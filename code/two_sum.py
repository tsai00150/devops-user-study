def twoSum(nums: list, target: int):
    if (not nums or len(nums) == 1):
        return
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in nums[idx+1:]:
            return [idx, idx + nums[idx+1:].index(diff) + 1]
