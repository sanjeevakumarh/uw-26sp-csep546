title:: HW2.A4

- ![image.png](../assets/image_1778305949883_0.png)
- A function $f: \mathbb{R}^d \to \mathbb{R}$ is convex on a set $A$ if $f(\lambda x + (1-\lambda) y) \leq \lambda f(x) + (1-\lambda) f(y)$ for all $x, y \in A$ and $\lambda \in [0,1]$. For each of the functions shown below (I-III), state whether each is convex on the specified interval, or state why not with a counterexample.
- A4.a. - **Convex**. The function is a smooth U-shaped curve with a single minimum near $b$. For any two points in $[a,c]$, the line between them lies on or above the function, satisfying $f(\lambda x + (1-\lambda) y) \leq \lambda f(x) + (1-\lambda) f(y)$.
- A4.b - **Not convex**. The function has a local maximum near $b$ between two valleys. The chord from $(a, f(a))$ to $(c, f(c))$ lies below the curve near $b$, i.e. $f(\lambda a + (1-\lambda) c) > \lambda f(a) + (1-\lambda) f(c)$ for some $\lambda \in [0,1]$, violating convexity.
- A4.c - **Not convex**. The function has an inflection and a local maximum between $b$ and $c$. The line segment from $(a, f(a))$ to $(d, f(d))$ lies below the curve in parts of the interval, violating the convexity condition.
- **Convex**. On the restricted interval $[c, d]$, the function is a concave-up curve (bowl-shaped). The line between any two points in $[c, d]$ lies on or above the function, satisfying the convexity condition.