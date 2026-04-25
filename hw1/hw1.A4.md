title:: HW1.A4

- A4. Learning Curves 
	- **Observations from Required plots** for $(d, \lambda) \in \{(1,0), (4,10^{-6}), (8,10^{-6}), (8,0.1), (8,1), (8,100)\}$
	-
		- Increasing $d$ from 1→4→8 with minimal regularization shows bias decreasing (training error drops) but variance increasing (train-test gap widens dramatically). At d=8, λ=1e-6, test error reaches 10⁶ — severe overfitting.
		- Increasing $\lambda$ from 1e-6→0.1→1→100 at fixed d=8 shows the reverse: the train-test gap narrows (variance decreasing) while both errors gradually rise (bias increasing). At λ=1, training and test error converge near the dashed line — the best tradeoff. At λ=100, both errors are high — effectively underfitting, similar to d=1.
	- **Observations from Additional exploratory plots** for $(d, \lambda) \in \{(2,10^{-6}), (4,0.1), (6,0.1), (8,0.01), (8,0.5), (8,10)\}$
		- Multiple (d, λ) combinations achieve similar performance — (d=4, λ=0.1), (d=6, λ=0.1), and (d=8, λ=0.5) all show tight convergence of training and test error. This confirms there is no single "correct" model — rather a family of solutions that balance bias and variance differently.
		- The sweet spot for d=8 lies around λ ∈ [0.5, 1], with λ=0.01 still overfitting and λ=10 already underfitting.
