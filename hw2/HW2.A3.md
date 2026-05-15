title:: HW2.A3
![image.png](../assets/image_1778305443171_0.png)

-
- A set $A \subseteq \mathbb{R}^n$ is *convex* if $\lambda x + (1 - \lambda) y \in A$ for all $x, y \in A$ and $\lambda \in [0,1]$. For each of the grey-shaded sets below (I-III), state whether each one is convex, or state why it is not convex using any of the points $a, b, c, d$.
-
- A3.I - **Not convex**. The straight line segment connecting points $b$ and $c$ passes through region outside the set, so there exist $\lambda \in [0,1]$ such that $\lambda a + (1-\lambda) c \notin A$.
- A3.II - **Convex**. For any two points inside the triangle, the line segment between them lies entirely within the triangle, satisfying the definition.
- A3.III - **Not convex**. The line segment connecting points $a$ and $d$ passes through the folded/notched region at the top-left of the shape, so there exist $\lambda \in [0,1]$ such that $\lambda a + (1-\lambda) d \notin A$.