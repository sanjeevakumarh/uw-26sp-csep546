title:: HW2.A1

- A1.a.
	- Suppose that your estimated model for predicting house prices has a large positive weight on
	  the feature number of bathrooms. If we remove this feature and refit the model, will the new model have a strictly higher error than before? Why?
	- Not necessarily. It depends on how the feature "number of bathrooms" is correlated with other features (e.g., square footage, number of bedrooms). When we remove it and refit, the model maybe able to redistribute predictive signal to those correlated features, partially or fully compensating. If large positive weight on this feature is introducing error, error may get reduced as a result as well.
- A1.b.
	- Compared to L2 norm penalty, explain why a L1 norm penalty is more likely to result in sparsity
	  (a larger number of 0s) in the weight vector.
	- L1 encourages more sparsity than L2 because the subgradient of the L1 penalty (|w_j|) is ±1 regardless of the magnitude of w_j, so it pushes weights toward zero with constant force even when they are already very small, driving them to exactly zero. In contrast, the gradient of the L2 penalty (w_j²) is 2w_j, which vanishes as w_j approaches zero — the shrinkage force weakens near zero, so weights settle at small but nonzero values.
- A1.c.
	- In at most one sentence each, state one possible upside and one possible downside of using the following regularizer: $\left(\sum_{i} |w_i|^{0.5}\right)$
	- **Upside:** It encourages stronger sparsity than L1 or L2, since the $p = 0.5$ penalty is more aggressive at penalizing small nonzero weights relative to large ones.
	- **Downside:** It is non-convex, so optimization becomes harder — the objective may have multiple local minima and standard gradient-based methods are not guaranteed to find the global minima.
- A1.d.
	- True or False: If the step-size for gradient descent is too large, it may not converge.
	- **True.** If the step size is too large, gradient descent can overshoot the minimum and oscillate with increasing magnitude, failing to converge.
- A1.e.
	- In your own words, describe why stochastic gradient descent (SGD) works, even though only a
	  small portion of the data is considered at each update.
	- SGD works because the gradient computed on a randomly sampled data point is an unbiased estimator of the full gradient. In expectation, each stochastic update points in the same direction as the true gradient. Over many iterations, the noise in individual updates averages out, and the algorithm converges to a neighborhood of the optimum.
- A1.f.
	- In at most one sentence each, state one possible advantage of SGD over GD (gradient descent),
	  and one possible disadvantage of SGD relative to GD
	- **Advantage:** SGD is cheaper per iteration — $O(d)$ for a single-sample update vs $O(nd)$ for GD — so on large datasets it makes much faster progress.
	- **Disadvantage:** SGD updates are noisy (high variance), which can cause oscillation around the optimum and generally requires more careful tuning to achieve convergence.
-