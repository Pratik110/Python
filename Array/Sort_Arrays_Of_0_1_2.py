Algorithm = "Dutch National Flag Algorithm"
Link = "https://leetcode.com/problems/sort-colors/"
Description = "Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of" \
              "the same color are adjacent, with the colors in the order red, white, and blue." \
              "We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively."
Example = "Input: nums = [2,0,2,1,1,0]" \
          "Output: [0,0,1,1,2,2]"
nums = [0,1,1,2,0,1,2,1,1,0]
# Approach_1
class Solution1:
    def sortColors(self, nums):
        nums.sort()
        return nums

print(Solution1().sortColors(nums))

# Approach 2
class Solution2:
    def sortColors(self,nums):
        c0 = 0
        c1 = 0
        c2 = 0
        for i in nums:
            if i == 0:
                c0+=1
            elif i == 1:
                c1+=1
            else:
                c2+=1
        for i in range(c0):
            nums[i] = 0
        for i in range(c0,c0+c1):
            nums[i] = 1
        for i in range(c0+c1,c0+c1+c2):
            nums[i] = 2
        return nums

print(Solution2().sortColors(nums))

# Approach 3
class Solution3:
    def sortColors(self,nums):
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high-=1
        return nums



print(Solution3().sortColors(nums))

