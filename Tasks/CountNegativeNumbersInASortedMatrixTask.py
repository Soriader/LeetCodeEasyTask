def countNegatives(self, grid: list[list[int]]) -> int:

    result = 0

    for i in grid:

        for j in i[::-1]:
            if j < 0:
                result += 1
            else:
                break

    return result

#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=daily-question&envId=2025-12-28