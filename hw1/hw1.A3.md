title:: HW1.A3


- **Observation of increasing regularization:** With $\lambda = 0$ and $d = 8$, the model overfits — the curve threads through the training points, capturing irreducible noise rather than generalizing underlying pattern. Increasing $\lambda$ progressively constrains coefficient magnitudes, smoothing the curve and improving generalization up to a point ($\lambda \approx 0.1$), beyond which the model becomes too constrained and underfits — losing the ability to capture the true relationship in the data.
	- **Plots** (all with $d = 8$):
		- $\lambda = 0$ — no regularization. The curve overfits, threading through training points and capturing noise.
		- $\lambda = 0.1$ — the curve is smoother and appears to generalize well, maintaining close fit to the data points with minimal squared error.
		- $\lambda = 0.5$ — the curve begins to underfit; data points near the origin start falling outside the fitted pattern.
		- $\lambda = 1.0$ — the lower half of the curve becomes nearly linear, missing the structure of data points near the origin.
		- $\lambda = 5.0$ — the curve is largely flattened, only fitting the central tendency of the data and missing most of the underlying pattern.