Link = "https://leetcode.com/problems/next-permutation/"
Description = "Implement next permutation, which rearranges numbers into the lexicographically" \
              "next greater permutation of numbers. If such an arrangement is not possible," \
              "it must rearrange it as the lowest possible order (i.e., sorted in ascending order)." \
              "The replacement must be in place and use only constant extra memory."
Example = "Input: nums = [1,2,3]" \
          "Output: [1,3,2]"
# Approach1
class Solution1:
    def nextPermutation(self, nums):
        l = len(nums)
        if l == 1:
            return  nums
        #traverse from the rear and find the first number which is lesser than its next number
        idx  = 0
        for i in range(l-1,-1,-1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
        if idx == -1:
            end = l//2
            for i in range(0,end):
                nums[i],nums[l-1] = nums[l-1],nums[i]
                l-=1
            return  nums
        just_greater = nums[idx+1]
        x = 0
        for i in range(idx+1,l):
            if nums[i] > nums[idx] and nums[i] <= just_greater:
                just_greater = nums[i]
                x = i

        temp = nums[x]
        nums[x] = nums[idx]
        nums[idx] = temp

        start = idx+1
        end = (start + l + 1)//2
        print(start,end)
        for i in range(start,end):
            nums[i], nums[l-1] = nums[l-1], nums[i]
            l-=1
        return nums
#[1,5,8,5,1,2,3,4,6,7]

# nums =
nums = [1]
print(Solution1().nextPermutation(nums))