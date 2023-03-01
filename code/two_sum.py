def twoSum(nums: list, target: int):
    

    mapping = {}
    for idx, num in enumerate(nums):
        mapping[num] = idx
    
    for num in nums:
        if target-num in mapping:
            if mapping[num] != mapping[target-num]:
                return [mapping[num], mapping[target-num]]
    else:
        return "There is no solution for nums and target."

        
# print(twoSum(nums=[2,7,11,15], target=9))