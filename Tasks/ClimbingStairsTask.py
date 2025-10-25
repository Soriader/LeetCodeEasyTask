def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev1, prev2 = 2, 1

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

#https://leetcode.com/problems/climbing-stairs/description/

