def totalMoney(n):
    """
    :type n: int
    :rtype: int
    """

    monday = 1
    iterator = 0
    result = 0
    money = monday

    while iterator < n:
        result += money
        money += 1
        iterator += 1

        if iterator % 7 == 0:
            monday += 1
            money = monday

    return result

#https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2025-10-25