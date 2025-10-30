def numSpecial(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """

    result = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count_row = 0
                for col in range(len(mat[0])):
                    if mat[i][col] == 1:
                        count_row += 1

                count_col = 0
                for row in range(len(mat)):
                    if mat[row][j] == 1:
                        count_col += 1

                if count_row == 1 and count_col == 1:
                    result += 1

    return result

#https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/