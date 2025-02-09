arr = [4,5,6,7,8,2,3,1]
target = 9

# Brute Force
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i, j) 
            
            
            
# Using Hash Table

def twoSum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        if nums[i] in num_dict:
            return [num_dict[nums[i]], i]
        num_dict[target - nums[i]] = i
    return None

print(twoSum(arr, target))