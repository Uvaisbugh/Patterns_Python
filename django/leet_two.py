
def twoSum( nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    # If no valid pair is found, return an empty list
    print(complement)
    print(hashmap)
    return []
        
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))