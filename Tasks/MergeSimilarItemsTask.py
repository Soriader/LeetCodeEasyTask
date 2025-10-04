def mergeSimilarItems(self, items1, items2):
    """
    :type items1: List[List[int]]
    :type items2: List[List[int]]
    :rtype: List[List[int]]
    """

    items_count = {}

    self.segregateItems(items1, items_count)
    self.segregateItems(items2, items_count)


    result = []

    for i in items_count:
        result.append((i, items_count[i]))

    return sorted(result)

def segregateItems(self, items, items_count):
    for i in items:

        if i[0] not in items_count:
            items_count[i[0]] = i[1]
        else:
            items_count[i[0]] += i[1]

    return items_count

#https://leetcode.com/problems/merge-similar-items/description/