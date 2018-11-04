## The Grandest Staircase Of Them All

How many ways can we arrange a staircase from *N* number of bricks?

### Constraints
Let *S* be the number of steps in our staircase.
Let *H<sub>i</sub>* be the height of step *i*.
- $S \ge 2$
- $H_i \ge 1$
- $H_i \gt H_{i+1}$

### Examples
I've worked through the solutions manually for $3 \lt N \le 10$. [link](manual.md)

### Recursion
Rather than thinking of the staircase with each step being lower than the previous step, let's make the staircase ascend. $H_i \lt H_{i+1}$

Let *P* be the height of the current stair and *L* be the number of bricks left.

$$
G(P,L)=
\begin{cases}
1 & \text{if } L = 0 \\
0 & \text{if } L < P \\
G(P+1,L-P)+G(P+1,L)
\end{cases}
$$

$$
F(N) = G(1, N)-1
$$

## Dynamic
If we run the recursive solution we would see that the number of invocations to *G* grows exponentially with *N*. Let's see what happens if we fill in an *NxN* matrix with results from the recursive solution.
[N=5](tables/table-05-recursive.md)
[N=10](tables/table-10-recursive.md)

We can observe the following with our recursive solution matrices:
- We don't care about the first row.
- Our final answer lies on the second row since $F(N) = G(1, N)$.
- The lower rows are used to compute the upper rows.
- The first column is filled with *1*s.
- The lower triangle is filled with *0*s.

We can create a new algorithm with the following conditions:
- The upper rows should be used to compute the lower rows.
- The final answer for *N* should live on row *N*.

$$
G(P,L)=
\begin{cases}
1 & \text{if } P=0 \and L=0 \\
0 & \text{if } P=0 \and L>0 \\
G(P-1,L) & \text{if } L < P \\
G(P-1,L)+G(P-1,L-P) & \text{if } L \ge P
\end{cases}
$$

$$
F(N) = G(N, N)-1
$$

Here are the tables for the new solution:
[N=5](tables/table-05-dynamic.md)
[N=10](tables/table-10-dynamic.md)

### Time and Space
With our dynamic solution we have quadratic time complexity as well as quadratic space complexity.

We can improve the algorithm further by only keeping the essential values in our matrix. Since each new row of the matrix only depends on the previous row we can keep a *2xN* matrix instead of *NxN*.

| Time     | Space  |
| -------- | ------ |
| $O(N^2)$ | $O(N)$ |

## References
1. [Jeremy Tuloup][ref1]
2. [Stack Exchange][ref2]

[ref1]: https://jtp.io/2016/07/26/dynamic-programming-python.html
[ref2]: https://math.stackexchange.com/questions/2055775/finding-all-possible-designs-for-a-staircase
