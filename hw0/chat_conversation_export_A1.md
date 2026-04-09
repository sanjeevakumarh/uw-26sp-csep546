# Chat Conversation Export

## User
After your yearly checkup, the doctor has bad news and good news. The bad news is that you tested positive for a serious disease, and that the test is 99% accurate (i.e., the probability of testing positive given that you have the disease is 0.99, as is the probability of testing negative given that you don't have the disease). The good news is that this is a rare disease, striking only one in 10,000 people. What are the chances that you actually have the disease?

Please include links only don't describe the solution or the details of the concepts. I want to solve the problem after reading the material, don't solve the problem.

## Assistant
- [Khan Academy — Tree diagrams and conditional probability](https://www.khanacademy.org/math/ap-statistics/probability-ap/stats-conditional-probability/a/tree-diagrams-conditional-probability)
- [MIT OpenCourseWare — Conditional Probability, Independence, Bayes’ Theorem (18.05)](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_lec03.pdf)
- [MIT OpenCourseWare — Conditional Probability Lecture Notes (Mathematics for Computer Science)](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/mit6_1200j_s24_lec19.pdf)
- [Seeing Theory — Bayesian Inference](https://seeing-theory.brown.edu/)
- [Wikipedia — Conditional probability](https://en.wikipedia.org/wiki/Conditional_probability)
- [Wikipedia — Base rate fallacy](https://en.wikipedia.org/wiki/Base_rate_fallacy)

## User
My intuition, look at false positive and true positives of a test in population and use that information to find out probability. Is that right direction? Don't solve the problem.

## Assistant
Yes. That is the right direction.

You want to think in terms of:
- how many people in a large population actually have the disease
- how many of those test positive
- how many people do **not** have the disease
- how many of those still test positive anyway

Then compare:
- **true positives**
against
- **all positives**

That framing is exactly the useful one here. Another good lens to review is **conditional probability / Bayes’ theorem**, but your population-count intuition is often the cleanest way to reason it out.

## User
Download this chat conversation as an MD file.
