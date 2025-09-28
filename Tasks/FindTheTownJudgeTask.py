def findJudge(self, n, trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """

    if n == 1 and not trust:
        return 1

    trust_count = {}
    trusters = set()

    for a, b in trust:
        trusters.add(a)
        trust_count[b] = trust_count.get(b, 0) + 1

    for person in range(1, n + 1):
        if person not in trusters and trust_count.get(person, 0) == n - 1:
            return person

    return -1

#https://leetcode.com/problems/find-the-town-judge/description/