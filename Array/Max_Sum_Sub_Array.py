Algorithm = "Kadane's Algorithm"
Link = "https://leetcode.com/problems/maximum-subarray/"
Logic = "https://youtu.be/w_KEocd__20"
Description = "Given an integer array nums, find the contiguous subarray " \
              "(containing at least one number) which has the largest sum " \
              "and return its sum."
Example_1 = "Input: nums = [-2,1,-3,4,-1,2,1,-5,4]" \
          "Output: 6" \
          "Explanation: [4,-1,2,1] has the largest sum = 6."
Example_2 = "Input: nums = [5,4,-1,7,8]'" \
            "Output: 23"

nums = [-2,1,-3,4,-1,2,1,-5,4]
# Approach 1
# Brute Force solution in BigO(n^3)
class Solution1:
    def maxSubArray(self, nums):
        maxm = 0
        l = len(nums)
        for i in range(l):
            for j in range(i,l):
                subArraySum = self.sum(nums[i:j+1])
                if subArraySum > maxm:
                    maxm = subArraySum
        return maxm

    def sum(self,array):
        s = 0
        for i in array:
            s+=i
        return s
print(Solution1().maxSubArray(nums))

# Approach 2
# Optimization of the Brute Force solution by reducing
# the time complexity to BigO(n^2) from BigO(n^3)
class Solution2:
    def maxSubArray(self,nums):
        maxm = 0
        l = len(nums)
        for i in range(l):
            s = 0
            for j in range(i,l):
                s+=nums[j]
                if s>maxm:
                    maxm = s
        return maxm
print(Solution2().maxSubArray(nums))

# Approach 3
# Solving the problem using Kadane's Algorithm which reduces the time complexity to BigO(n)
class Solution3:
    def maxSubArray(self,nums):
        currSum = 0
        maxSum = nums[0]
        l = len(nums)
        for i in range(l):
            currSum+=nums[i]
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return  maxSum
print(Solution3().maxSubArray(nums))