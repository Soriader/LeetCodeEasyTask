def readBinaryWatch(self, turnedOn: int) -> list[str]:

    if turnedOn > 8:
        return []

    result = []

    for hour in range(0, 12):

        for minute in range(0, 60):

            if hour.bit_count() + minute.bit_count() == turnedOn:
                result.append(f"{hour}:{minute:02d}")


    return result

#https://leetcode.com/problems/binary-watch/description/?envType=daily-question&envId=2026-02-17