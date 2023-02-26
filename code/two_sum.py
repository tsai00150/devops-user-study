def twoSum(nums: list, target: int):
    length = len(nums)
    dictionary = {}
    for i in range(0,length):
        dictionary[nums[i]]=i
    for j in range(0,length):
        res = target - nums[j]
        if res in dictionary: 
            print([j,dictionary[res]])
            return [j,dictionary[res]]
        
twoSum([2,7,11,15],9)
