Link = "https://leetcode.com/problems/longest-consecutive-sequence/"
Description = "Given an unsorted array of integers nums, return the" \
              "length of the longest consecutive elements sequence."
Example = "Input: nums = [100,4,200,1,3,2]" \
          "Output: 4" \
          "Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. " \
          "Therefore its length is 4."

#Aprroach 1

nums = [100,4,200,1,3,2]
class Solution1:
    def longestConsecutive(self,nums):
        hash_dict = dict()
        
print(Solution1().longestConsecutive(nums))