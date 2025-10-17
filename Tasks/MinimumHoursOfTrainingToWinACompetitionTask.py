def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
    """
    :type initialEnergy: int
    :type initialExperience: int
    :type energy: List[int]
    :type experience: List[int]
    :rtype: int
    """
    result = max(0, sum(energy) - initialEnergy + 1)
    for enemy in experience:
        if enemy > initialExperience:
            training = enemy - initialExperience + 1
            result += training
            initialExperience += training
        elif enemy == initialExperience:
            result += 1
            initialExperience += 1

        initialExperience += enemy

    if result <= 0:
        return 0

    return result

#https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/description/