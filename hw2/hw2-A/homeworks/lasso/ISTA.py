from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np

from utils import problem


@problem.tag("hw2-A")
def step(
    X: np.ndarray, y: np.ndarray, weight: np.ndarray, bias: float, _lambda: float, eta: float
) -> Tuple[np.ndarray, float]:
    """Single step in ISTA algorithm.
    It should update every entry in weight, and then return an updated version of weight along with calculated bias on input weight!

    Args:
        X (np.ndarray): An (n x d) matrix, with n observations each with d features.
        y (np.ndarray): An (n, ) array, with n observations of targets.
        weight (np.ndarray): An (d,) array. Weight returned from the step before.
        bias (float): Bias returned from the step before.
        _lambda (float): Regularization constant. Determines when weight is updated to 0, and when to other values.
        eta (float): Step-size. Determines how far the ISTA iteration moves for each step.

    Returns:
        Tuple[np.ndarray, float]: Tuple with 2 entries. First represents updated weight vector, second represents bias.
    
    """
    residual = X @ weight + bias - y
    #  derivative of the squared error (xiT​w+b−yi​)^2. The derivative of z^2 is 2z => 2 * eta
    bias_new = bias - 2 * eta * np.sum(residual)
    w_grad = weight - 2 * eta * (X.T @ residual)
    threshold = 2 * eta * _lambda
    weight_new = np.sign(w_grad) * np.maximum(np.abs(w_grad) - threshold, 0)
    return weight_new, bias_new


@problem.tag("hw2-A")
def loss(
    X: np.ndarray, y: np.ndarray, weight: np.ndarray, bias: float, _lambda: float
) -> float:
    """L-1 (Lasso) regularized SSE loss.

    Args:
        X (np.ndarray): An (n x d) matrix, with n observations each with d features.
        y (np.ndarray): An (n, ) array, with n observations of targets.
        weight (np.ndarray): An (d,) array. Currently predicted weights.
        bias (float): Currently predicted bias.
        _lambda (float): Regularization constant. Should be used along with L1 norm of weight.

    Returns:
        float: value of the loss function
    """
    residual = X @ weight + bias - y
    return np.sum(residual ** 2) + _lambda * np.sum(np.abs(weight))


@problem.tag("hw2-A", start_line=5)
def train(
    X: np.ndarray,
    y: np.ndarray,
    _lambda: float = 0.01,
    eta: float = 0.00001,
    convergence_delta: float = 1e-4,
    start_weight: np.ndarray = None,
    start_bias: float = None
) -> Tuple[np.ndarray, float]:
    """Trains a model and returns predicted weight and bias.

    Args:
        X (np.ndarray): An (n x d) matrix, with n observations each with d features.
        y (np.ndarray): An (n, ) array, with n observations of targets.
        _lambda (float): Regularization constant. Should be used for both step and loss.
        eta (float): Step size.
        convergence_delta (float, optional): Defines when to stop training algorithm.
            The smaller the value the longer algorithm will train.
            Defaults to 1e-4.
        start_weight (np.ndarray, optional): Weight for hot-starting model.
            If None, defaults to array of zeros. Defaults to None.
            It can be useful when testing for multiple values of lambda.
        start_bias (float, optional): Bias for hot-starting model.
            If None, defaults to zero. Defaults to None.
            It can be useful when testing for multiple values of lambda.

    Returns:
        Tuple[np.ndarray, float]: A tuple with first item being array of shape (d,) representing predicted weights,
            and second item being a float representing the bias.

    Note:
        - You will have to keep an old copy of weights for convergence criterion function.
            Please use `np.copy(...)` function, since numpy might sometimes copy by reference,
            instead of by value leading to bugs.
        - You will also have to keep an old copy of bias for convergence criterion function.
        - You might wonder why do we also return bias here, if we don't need it for this problem.
            There are two reasons for it:
                - Model is fully specified only with bias and weight.
                    Otherwise you would not be able to make predictions.
                    Training function that does not return a fully usable model is just weird.
                - You will use bias in next problem.
    """
    if start_weight is None:
        start_weight = np.zeros(X.shape[1])
        start_bias = 0
    old_w: Optional[np.ndarray] = None
    old_b: float = None
    w = np.copy(start_weight)
    b = float(start_bias) if start_bias is not None else 0.0

    while True:
        old_w = np.copy(w)
        old_b = b
        w, b = step(X, y, w, b, _lambda, eta)
        if convergence_criterion(w, old_w, b, old_b, convergence_delta):
            break
    return w, b


@problem.tag("hw2-A")
def convergence_criterion(
    weight: np.ndarray, old_w: np.ndarray, bias: float, old_b: float, convergence_delta: float
) -> bool:
    """Function determining whether weight and bias has converged or not.
    It should calculate the maximum absolute change between weight and old_w vector, and compare it to convergence delta.
    It should also calculate the maximum absolute change between the bias and old_b, and compare it to convergence delta.

    Args:
        weight (np.ndarray): Weight from current iteration of gradient descent.
        old_w (np.ndarray): Weight from previous iteration of gradient descent.
        bias (float): Bias from current iteration of gradient descent.
        old_b (float): Bias from previous iteration of gradient descent.
        convergence_delta (float): Aggressiveness of the check.

    Returns:
        bool: False, if weight and bias has not converged yet. True otherwise.
    """
    max_change = max(np.max(np.abs(weight - old_w)), abs(bias - old_b))
    return max_change < convergence_delta


@problem.tag("hw2-A")
def main():
    """
    Use all of the functions above to make plots.
    """
    # rondom seed - 777
    np.random.seed(777)
    # n (samples) = 500, d (features) = 1000, k (relevant features) = 100, sigma (noise) = 1.0
    n, d, k, sigma = 500, 1000, 100, 1.0

    # True weights: w_j = j/k for j=1..k, else 0
    w_true = np.zeros(d)
    for j in range(k):
        w_true[j] = (j + 1) / k

    # Generate X, standardize, generate y
    X = np.random.randn(n, d)
    # avoid division by zero in case of zero std => 1e-9
    X = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-9)
    epsilon = sigma * np.random.randn(n)
    y = X @ w_true + epsilon

    # lambda_max: smallest lambda where all weights are zero
    y_bar = np.mean(y)
    lambda_max = np.max(2 * np.abs(X.T @ (y - y_bar)))

    # Build regularization : lambda_max, lambda_max/2, lambda_max/4, ...
    lambdas = []
    lam = lambda_max
    while lam >= 0.01:
        lambdas.append(lam)
        lam /= 2

    # Track metrics
    nonzeros_list = []
    fdr_list = []
    tpr_list = []
    w_prev, b_prev = None, None

    for lam in lambdas:
        w_hat, b_hat = train(X, y, _lambda=lam, eta=0.00001,
                            convergence_delta=1e-4,
                            start_weight=w_prev, start_bias=b_prev)
        w_prev = np.copy(w_hat)
        b_prev = b_hat

        nz_mask = w_hat != 0
        total_nz = np.sum(nz_mask)
        nonzeros_list.append(total_nz)

        correct_nz = np.sum(nz_mask & (w_true != 0))
        incorrect_nz = np.sum(nz_mask & (w_true == 0))
        fdr = incorrect_nz / total_nz if total_nz > 0 else 0.0
        tpr = correct_nz / k

        fdr_list.append(fdr)
        tpr_list.append(tpr)
        print(f"lambda={lam:.4f}, nonzeros={total_nz}, FDR={fdr:.3f}, TPR={tpr:.3f}")

    # Plot 1: nonzeros vs lambda
    plt.figure()
    plt.plot(lambdas, nonzeros_list, 'o-')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('Number of nonzeros')
    plt.title('Lasso Sparsity: Nonzero Weights vs Regularization Strength λ')
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig('plot1_nonzeros_vs_lambda.png', dpi=144)
    plt.show()

    # Plot 2: FDR vs TPR
    plt.figure()
    plt.plot(fdr_list, tpr_list, 'o-')
    plt.xlabel('FDR')
    plt.ylabel('TPR')
    plt.title('Lasso Feature Selection: FDR vs TPR Across Regularization Path')
    plt.tight_layout()
    plt.savefig('plot2_fdr_vs_tpr.png', dpi=144)
    plt.show()


if __name__ == "__main__":
    main()
