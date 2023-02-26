def twoSum(nums: list, target: int):
    seen = {}
    for i, num in enumerate(nums):
        seen[num] = i

    for num in seen:
        if target - num in seen:
            print([seen[num], seen[target - num]])
            return [seen[num], seen[target - num]]

twoSum([2,7,11,15], 9)