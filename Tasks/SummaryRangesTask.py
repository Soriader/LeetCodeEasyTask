def summaryRanges(self, nums):
    if not nums:
        return []

    start = nums[0]
    result = []

    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append("{}->{}".format(start, nums[i]))
            start = nums[i + 1]

    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append("{}->{}".format(start, nums[-1]))

    return result

#https://leetcode.com/problems/summary-ranges/

