
'''

∟ Recursion forms the basis for:
    - Memoization:
        > Storing the results of sub-problems and reusing them later
        > Uses recursion
        > Top Down approach
    - Tabulation
        > Most widely used Dynamic Programming technique
        > Iterative approach
        > Does not use recursion
        > Bottom Up approach

∟ Need to understand the pattern to implement Memoization or Tabulation
    - Recursion  →  to understand pattern
          ↓
    - Memoization
          ↓
    - Tabulation  →  ideal approach

∟ Steps in Dynamic Programming

    1. Break down the complex problem into simpler sub-problems
    2. Find optimal solution to these sub-problems
    3. Store results / solutions of sub-problems (Memoization)
    4. Reuse the results / solutions of sub-problems so that a given sub-problem is not calculated more than once
    5. Calculate the result of the complex problem by combining the solutions of sub-problems
        > Applicable to problems which have:
            - Overlapping sub-problems (possibility of having duplicate calculations)
            - Final solution can be obtained by combining optimal solutions of sub-problems
                → A.K.A - Optimal Sub-structures

∟ Dynamic Programming is well suited for optimization problems
    - Finding best solutions that take minimum possible time
    - Use minimum possible memory
        > Ex: Transportation  →  shortest path
    - Recursion  →  Memoization  →  Tabulation
        2^n             n               1


═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

1   1   2   3   5   8

Ex: Obtain 5th number in Fb series

∟ Tracing Tree
∟ Recursive Solution:
    - Two main issues
        > High time complexity
        > Duplicate evaluation of sub-problems
            time complexity → O(2^n)
            15 calls
            fib(1) → 5 times
            fib(2) → 3 times

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

                                                 fib(5)
                                               /
                                         fib(4)
                                       /       \
                                fib(3)       fib(2)
                                /      \
                          fib(2)    fib(1)
                         /   \
                     fib(1)   fib(0)

    store:  fib(1): 1  fib(0): 0  fib(2): 1   fib(3): 2   fib(4): 3  fib(5): 5

    - 15 calls using recursion
    - 9 calls using memoization

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

∟ Time Complexity:
    - Number of opens (calls) that are required to solve the problem
    - As the number of operations increases, time complexity increases
        Ex: Quicksort  →  O(n^2)

∟ Space Complexity:
    - Memory usage

∟ It is desired that both Time Complexity and Space Complexity values are low.

∟ Undesirable:   Try to avoid
    - o(n!)
    - o(2n)
    - o(n^2)
∟ Desirable:
    - o(n log n) → Linear Relation
    - o(n) →  Attempting to determine 5th number in Fibonacci series, takes 5 calls
    - o(log n)
    - o(1) → Constant time or space complexity → Irrespective of n value, only need 1 function call.

∟ Recursive:

1 + 1 = 2

1 + 1 + 1 = 3

1+ 1 + 1 + 1 = 4

∟ Memoization:

1 + 1 = 2   →  [Store]

1 + 1 + 1 = 3  →  [2] + 1 = 3  →  [Store]

1 + 1 + 1 + 1 = 4  →  [3] + 1 = 4  →  [Store]

∟ Tabulation:

                             (3)    1+2
                            i = 4 ← ← ← ← ← ← (2)
                              ⬉              i = 3
                                ⬉  1+1    ⬈    ⬈
                                  ⬉     ⬈     ⬈
                                   ⬉ ⬈       ⬈
                                   (1)       ⬈
                                  i = 2     ⬈
                                  ⬈   ⬉   ⬈
                                ⬈  0+1  ⬉⬈
                              (0)        (1)
                             i = 0     i = 1

i = element position
() value at ith position

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

∟ Longest Common Subsequence (LCS)
    - STR1 : a b c d e f g h i j
    - STR2 : cdgi

    > substrings : consecutive groups of chars with no gaps
        →  abcd, bcd, efgh, hij
    > subsequences: sequence of chars which may have gaps
        →  acdh, ehj
        →  every substring is a subsequence but every subsequence may not be a substring
    > Length of longest Subsequence
        →  cdgi, dgi  →  cdgi  →  LCS  →  length is 4

    - STR1: a b c d e f g h i j
    - STR2: e c d g i
        →  cdgi → length is 4

    - STR1: C G A T A A T T G A G A
    - STR2: G T T C C T A A T A
        →  GTTTAA, TTTAA, TTAA, CTAATA  →  length is 6

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

## Recursive Solution

A:  b  d  \0
i = 0  1  2

B:  a  b  c  d  \0
j = 0  1  2  3  4

1. If A[i] == B[j]
    return 1 + result of next char checks in both strings 1 + (A[i + 1] == B[j + 1])
2. If the chars are not equal,
    return the maximum of below checks
      - A[i + 1] == B[j]
      - A[i] == B[j + 1]

                                Max(1,2) = 2  LCS is of Length 2

                            A[0]                                   B[0]
                             b                                      a              (b!=a)
                           /                                        \
  (d!=a)           A[1]B[0]   →  1            2  ←  A[0]B[1]
                    d    a                                         b   b  (=)
                 /    \                                              ↓
         A[2]B[0]      A[1]B[1]  →  1                            1 + A[1]B[2]  →  1
   0  ←   \0    a        d    b                                       d   c    (d!=c)
                     /    \                                         /   \
             A[2]B[1]      A[1]B[2]  →  1                     A[2]B[2]   A[1]B[3]   → 1
   0   ←      \0   b         d   c                      0   ←  \0  c      d    d   (=)
                          /   \                                             ↓
                  A[2]B[2]     A[1]B[3]                                1 + A[2]B[4]
   0   ←           \0  c        d   d  (==) →   1                           \0  \0
                                  ↓
                            1 + A[2]B[4]
                      0   ←      \0  \0

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

## Memoization Solution

B  → │  a │ b  │  c │ d │ \0 │
A  ↓ │  0 │  1 │  2 │ 3 │   4│
 ════│════│════│════│═══│════│
b   0│ 2  │ 2  │ x  │ x │ x  │
 ════│════│════│════│═══│════│
d   1│ 1  │ 1  │ 1  │ 1 │ x  │
 ════│════│════│════│═══│════│
\0  2│ 0  │ 0  │ 0  │ x │ 0  │
 ════│════│════│════│═══│════│


'''
