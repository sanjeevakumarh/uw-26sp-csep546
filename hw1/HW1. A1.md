title:: HW1. A1

- A1. a. In your own words, describe what bias and variance are? What is bias-variance tradeoff?
	- **Bias** measures how far off a model's expected predictions are from the true values — it's the systematic error that comes from wrong assumptions in the model, such as insufficient features, incorrect hyperparameters, or poor parameter selection.
		- Examples: (1) Fitting a straight line to data that's actually quadratic will consistently miss the curve no matter how much data you have. (2) A home sale price model that assigns high weight to exterior color or number of windows while missing key features like square footage — it will systematically mis-estimate because the model's assumptions about what matters are wrong.
	- **Variance** measures how much a model's predictions change when you train it on different samples of data. A high-variance model is overly sensitive to the specific training data it saw — it picks up on noise and random fluctuations, deriving artificial patterns rather than learning the true underlying relationship.
		- Examples: (1) A model estimating a building's livable area that treats every roofline data point as meaningful signal — minor measurement noise in the roofline causes wildly different area estimates across training sets. (2) A degree-20 polynomial fit to 15 data points — it threads perfectly through the training data but produces completely different curves with a slightly different sample, because it's fitting noise rather than the true trend.
	- **The bias-variance tradeoff:** Total prediction error decomposes as Error = Bias² + Variance + irreducible noise. Simple models (few parameters) tend to have high bias and low variance — they underfit. Complex models (many parameters) tend to have low bias and high variance — they overfit. Reducing one typically increases the other. The goal is to find the model complexity that minimizes total error — flexible enough to capture the real pattern but constrained enough not to memorize noise.
		- The practical implication: it can be wise to use a biased estimator, so long as it reduces variance enough to lower the overall squared error (Murphy, chapter 6.4).
	-
- A1. b. What **typically** happens to bias and variance when the model complexity increases/decreases?
- **When model complexity increases** (more parameters, higher degree polynomial, more features): bias typically decreases because the model has more flexibility to fit the true underlying pattern. But variance typically increases because the model becomes more sensitive to the specific training data, and each trading data point is inclusive of irreducible noise, variance on validation data will be higher.
- **When model complexity decreases** (fewer parameters, stronger regularization, fewer features): bias typically increases because the model is too constrained to capture the true relationship. But variance typically decreases because the model is more stable across different training samples — there's less room to overfit.
- **Edge cases** When an included feature that has very minimal predictive weight (ex: house number/street name in the sale price estimation) complexity is increased, but may not really reflect on bias decreasing, and conversely removal of such feature/dimension may not increase variance since the model was depending on a noisy dimension to start with.
- There are known techniques to control Variance like averaging over multiple models (ensembling), but bias cannot — averaging equally biased models still produces a biased result.
-
- A1.c.
- **False.**
- Fewer features can improve generalization when the removed features are noisy or irrelevant, thus reducing variance and/or overfitting. But removing features that carry high predictive signal increases bias, and the model generalizes worse.
	- For example, predicting home prices using square footage + school rating generalizes well (both carry meaningful signal). Dropping school rating would hurt generalization because important predictive information is lost.
- It depends on *which* features are removed and whether the reduction in variance outweighs the increase in bias.
-
- A1.d. True or False: Hyperparameters should be tuned on the test set. Explain your choice and detail
  a procedure for hyperparameter tuning.
- **False.**
- The test set exists to give an unbiased estimate of how the model will perform on unseen data. If hyperparameters are tuned on the test set, the model is effectively "peeking" at test data during training — the test set is no longer unseen, and the produces (artificially) optimistic estimate for the model.
-
- A1.e. True or False: The training error of a function on the training set provides an overestimate of
  the true error of that function
- **False**
- Training error provides an **under**estimate of the true error. Since model's parameters were optimized specifically to minimize error on the training data, it will almost always perform better on the data it was trained on than on new, unseen data.
- Example : complex models with a high-degree polynomial can achieve near-zero training error for every training point, while its true error on new data is would typically be much higher due to overfitting.
-