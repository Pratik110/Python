Link = "https://leetcode.com/problems/find-the-duplicate-number/"
Description = "Given an array of integers nums containing n + 1 integers where " \
              "each integer is in the range [1, n] inclusive. There is only one " \
              "repeated number in nums, return this repeated number."
Examples = "Input: nums = [1,3,4,2,2]" \
           "Output: 2" \
           "" \
           "Input: nums = [3,1,3,4,2]" \
           "Output: 3"
nums = [1,3,4,2,2]
# Approach 1 - Brute Force using count
class Solution1:
    def findDuplicate(self,nums):
        for i in nums:
            if nums.count(i) >= 2:
                return i
print(Solution1().findDuplicate(nums),"is the duplicate number")

# Approach 2 - Brute Force using sort
class Solution2:
    def findDuplicate(self,nums):
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return  nums[i]
print(Solution2().findDuplicate(nums),"is the duplicate number")

# Approach 3 - Hashing using a frequency array
class Solution3:
    def findDuplicate(self,nums):
        l = len(nums)
        op = [0]*l
        for i in nums:
            op[i%l]+=1
            if op[i%l] == 2:
                return i
print(Solution3().findDuplicate(nums),"is the duplicate number")