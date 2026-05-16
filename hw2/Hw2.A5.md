title:: Hw2.A5

- Synthetic data setup
	- Generate data with $n = 500$, $d = 1000$, $k = 100$, $\sigma = 1$:
	- $$w_j = \begin{cases} j/k & j \in \{1, \dots, k\} \\ 0 & \text{otherwise} \end{cases}$$
		- $x_i \sim \mathcal{N}(0, I)$, standardized. $y_i = w^T x_i + \epsilon_i$, $\epsilon_i \sim \mathcal{N}(0, 1)$.
		  $\lambda_{\max} = \max_{k=1,\dots,d} 2 \left| \sum_{i=1}^{n} x_{i,k}(y_i - \bar{y}) \right|$
		- Regularization path: start at $\lambda_{\max}$, halve each time, warm-start from previous solution.
- Part a
	- As $\lambda$ decreases from $\lambda_{\max}$, the number of nonzero weights increases monotonically from 0 to $d = 1000$, following a sigmoid looking curve on a log scale with the steepest rise around $\lambda \in [1, 100]$.
	- graph - Lasso Sparsity - Nonzero Weights vs Regularization λ.png.
- Part b
	- The curve traces from (0,0)(0,0) at large λ*λ* toward (0.9,1)(0.9,1) at small λ*λ*, showing that the Lasso initially recovers true features with low false discovery before noise features start entering the model.
	- graph - Lasso Feature Selection- FDR vs TPR Across Regularization Path.png
- Part c
	- As λ decreases, the Lasso first recovers the true nonzero features (TPR rises quickly while FDR stays low), then begins selecting irrelevant features (FDR climbs). There is a “sweet spot” of λ values where TPR is high and FDR is low — this corresponds to the elbow region in Plot 1 where the number of nonzeros is close to the true k=100. Too large λ misses true signals; too small λ overfits by including inherent noise.
-