if __name__ == "__main__":
    from ISTA import train  # type: ignore
else:
    from .ISTA import train

import matplotlib.pyplot as plt
import numpy as np

from utils import load_dataset, problem


@problem.tag("hw2-A", start_line=3)
def main():
    # df_train and df_test are pandas dataframes.
    # Make sure you split them into observations and targets
    df_train, df_test = load_dataset("crime")
    
    y_train = df_train["ViolentCrimesPerPop"].values
    X_train = df_train.drop("ViolentCrimesPerPop", axis=1).values
    feature_names = df_train.drop("ViolentCrimesPerPop", axis=1).columns.tolist()
    
    y_test = df_test["ViolentCrimesPerPop"].values
    X_test = df_test.drop("ViolentCrimesPerPop", axis=1).values

    y_bar = np.mean(y_train)
    lambda_max = np.max(2 * np.abs(X_train.T @ (y_train - y_bar)))

    lambdas = []
    lam = lambda_max
    while lam >= 0.01:
        lambdas.append(lam)
        lam /= 2
        
    nonzeros_list = []
    weights_path = []
    train_errors = []
    test_errors = []
    w_prev, b_prev = None, None

    for lam in lambdas:
        w_hat, b_hat = train(X_train, y_train, _lambda=lam, eta=0.00001,
                            convergence_delta=1e-4,
                            start_weight=w_prev, start_bias=b_prev)
        w_prev = np.copy(w_hat)
        b_prev = b_hat
        nonzeros_list.append(np.sum(w_hat != 0))
        weights_path.append(np.copy(w_hat))
        train_errors.append(np.sum((X_train @ w_hat + b_hat - y_train) ** 2))
        test_errors.append(np.sum((X_test @ w_hat + b_hat - y_test) ** 2))

    weights_path = np.array(weights_path)
        
    plt.figure()
    plt.plot(lambdas, nonzeros_list, 'o-')
    plt.xscale('log')
    plt.xlabel(r'$\lambda$')
    plt.ylabel('Number of Nonzero Weights')
    plt.title(r'Crime Data: Nonzero Weights vs $\lambda$')
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig('plot3_crime_nonzeros.png', dpi=150)
    plt.show()
    
    # --- Plot d: regularization paths for 5 features ---
    track_features = ['agePct12t29', 'pctWSocSec', 'pctUrban', 'agePct65up', 'householdsize']
    plt.figure()
    for feat in track_features:
        idx = feature_names.index(feat)
        plt.plot(lambdas, weights_path[:, idx], 'o-', label=feat, markersize=3)
    plt.xscale('log')
    plt.xlabel(r'$\lambda$')
    plt.ylabel('Coefficient Value')
    plt.title(r'Crime Data: Regularization Paths for Selected Features')
    plt.legend()
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig('plot4_crime_reg_paths.png', dpi=150)
    plt.show()
    
    # --- Plot e: train/test squared error vs lambda ---
    plt.figure()
    plt.plot(lambdas, train_errors, 'o-', label='Train', markersize=3)
    plt.plot(lambdas, test_errors, 'o-', label='Test', markersize=3)
    plt.xscale('log')
    plt.xlabel(r'$\lambda$')
    plt.ylabel('Squared Error')
    plt.title(r'Crime Data: Train/Test Squared Error vs $\lambda$')
    plt.legend()
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig('plot5_crime_error.png', dpi=150)
    plt.show()

if __name__ == "__main__":
    main()
