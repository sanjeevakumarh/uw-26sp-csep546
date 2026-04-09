# Conversation Export

**Date:** 2026-04-09

## User
Can you provide pointers on concepts I should brush up on to solve these 4 problems? including math bsics.

Don't solve the problem give me pointers/links/youtube videos or freely available courses I should review.

## Assistant
Yes. For these four, I’d brush up in this order.

**1) Math basics first**
- **Sigma notation / summations**: you need to be comfortable reading expressions like \(\frac1n\sum_{i=1}^n X_i\). Khan’s summation review is a good quick refresher.
- **u-substitution for integrals**: part **b** explicitly hints at this, so make sure you can spot a substitution and change variables cleanly in definite or improper integrals. Khan and Paul’s Online Notes are both solid.

**2) Core probability/statistics ideas**
- **Normal distribution basics**: mean \(\mu\), variance \(\sigma^2\), standardization, and what \(N(0,1)\) means. Khan’s normal-distribution review/video or StatQuest are good for intuition.
- **Expectation and variance rules**: especially  
  \[
  E[aX+b],\quad \mathrm{Var}(aX+b),\quad E[X+Y],\quad \mathrm{Var}(X+Y)
  \]
  and when independence matters.

**3) What each part is really testing**
- **Part a**: *linear transformation / standardization of a normal random variable*. Review scaling and shifting of random variables.
- **Part b**: *expected absolute value after standardization*. That means normal pdf, symmetry, absolute value inside an expectation, and integration with substitution.
- **Part c**: *linearity of expectation* and *variance of a linear combination of independent variables*.
- **Part d**: *sample mean / sampling distribution*. You want to know the mean and variance of \(\hat\mu_n = \frac1n\sum X_i\), and then what multiplying by \(\sqrt n\) does to mean and variance.

**4) Free resources**
- Khan Academy: statistics & probability overview, then random variables, transformations, combining random variables, and sampling distributions.
- MIT OCW probability/statistics notes on expectation, variance, continuous random variables, and sums of independent normals.
- OpenStax *Introductory Statistics 2e* for normal distributions and sampling distributions.
- StatQuest for normal distribution intuition.

**5) Tight study checklist**
Before attempting the problem set, make sure you can do these without notes:
- Read and manipulate sigma notation.
- Explain what happens to mean and variance under \(Y=aX+b\).
- State when \(\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\) is valid.
- Explain what the sample mean’s distribution looks like when the \(X_i\) are normal.
- Do a basic u-substitution cleanly.

If you want, I can turn this into a **30-minute targeted review plan** in the exact order to study before you try the problems.

## User
Export this conversation as an MD file.
