def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:

    sum_apple = sum(apple)

    result = 0
    actual_sum = 0
    for x in sorted(capacity, reverse=True):

        actual_sum += x
        result += 1
        if actual_sum >= sum_apple:
            break

    return result

#https://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24