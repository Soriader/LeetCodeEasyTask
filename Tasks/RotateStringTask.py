def rotateString(s, goal):

    if s == goal:
        return True

    rotated_s = s

    while rotated_s != goal:

        rotated_s = rotated_s[1:] + rotated_s[0]
        if rotated_s == goal:
            return True
        elif rotated_s == s:
            break

    return False

#https://leetcode.com/problems/rotate-string/description/