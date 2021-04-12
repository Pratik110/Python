Link = "https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/"
Description = "Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from " \
              "set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers."
Examples = "Input: arr[] = {3, 1, 3}" \
           "Output: Missing = 2, Repeating = 3" \
           "Explanation: In the array, " \
           "2 is missing and 3 occurs twice " \
           "" \
           "Input: arr[] = {4, 3, 6, 2, 1, 1}" \
           "Output: Missing = 5, Repeating = 1"

nums = [1, 2, 3, 4, 5, 5, 6, 8]
# Approach 1
#Brute force approach using element count
class Solution1:
    def missingAndRepeatingNum(self, nums):
        l = len(nums)
        missing_num = 0
        repeating_num = 0
        for i in range(1,l+1):
            if nums.count(i) == 0:
                missing_num = i
            if nums.count(i) == 2:
                repeating_num = i
        return "missing number is {} and repeating number is {}".format(missing_num,repeating_num)
print(Solution1().missingAndRepeatingNum(nums))

# Approach 2
# Sort the array and find the repeating and missing element
class Solution2:
    def missingAndRepeatingNum(self,nums):
        nums.sort()
        missing_num = 0
        repeating_num = 0
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                repeating_num = nums[i]
            if nums[i+1] - nums[i] > 1:
                missing_num = nums[i]+1
            if i == l-2 and missing_num == 0:
                missing_num = l
        return "missing number is {} and repeating number is {}".format(missing_num, repeating_num)
print(Solution2().missingAndRepeatingNum(nums))

# Approach 3
# Count index
class Solution3:
    def missingAndRepeatingNum(self,nums):
        l = len(nums)
        missing_num = 0
        repeating_num = 0
        indexList = [0] * l
        for i in nums:
            indexList[i-1]+=1
        for i,j in enumerate(indexList):
            if j == 0:
                missing_num = i+1
            if j == 2:
                repeating_num = i+1
        return "missing number is {} and repeating number is {}".format(missing_num, repeating_num)
print(Solution3().missingAndRepeatingNum(nums))
