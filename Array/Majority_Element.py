Link = "https://leetcode.com/problems/majority-element/submissions/"
Solution = "https://youtu.be/AoX3BPWNnoE"
Description = "Given an array nums of size n, return the majority element." \
              "The majority element is the element that appears more than [n / 2]times." \
              "You may assume that the majority element always exists in the array."
Example = "Input: nums = [3,2,3]" \
          "Output: 3"

nums = [2, 2, 1, 1, 1, 2, 2]

# Approach 1, using a dictionary to store the count of elements, if count greater than l//2 ,then return the element
class Solution1:
    def majorityElement(self, nums):
        l = len(nums) // 2
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        for i in nums:
            if a[i] > l:
                return i
print(Solution1().majorityElement(nums))

# Approach 2, using a hashmap to store the count of elements, if count greater than l//2 ,then return the element
class Solution2:
    def majorityElement(self, nums):
        l = len(nums) // 2
        maxm = 0
        for i in nums:
            if i>maxm:
                maxm=i
        a = [0]*(maxm+1)
        for i in nums:
            a[i]+=1
        for i in range(maxm+1):
            if a[i]>l:
                return i
print(Solution2().majorityElement(nums))

# Approach 3. using the Moore's Voting Algorithm
class Solution3:
    def majorityElement(self, nums):
        majority_elem = nums[0]
        l = len(nums)
        count = 0
        for i in range(l):
            if nums[i] == majority_elem:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority_elem = nums[i+1]
        return majority_elem

print(Solution3().majorityElement(nums))