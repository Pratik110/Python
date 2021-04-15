Link = "https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1"
Description = "Given an unsorted array A of size N that contains only non-negative integers," \
              "find a continuous sub-array which adds to a given number S."
Example = "Input:" \
          "N = 5, S = 12" \
          "A = [1,2,3,7,5]" \
          "Output: 2 4" \
          "Explanation: The sum of elements  from 2nd position to 4th position is 12"
arr = [1,2,3,4,5,6,7,8,9,10]
s = 15
class Solution1:
    def subArraySum(self,arr,s):
        currsum = 0
        start = 0
        end = 0
        while start <= end:
            element1 = arr[end]
            element2 = arr[start]
            if currsum < s:
                currsum+=element1
                end+=1
            elif currsum > s:
                currsum-=element2
                start+=1
            else:
                return start+1,end


print(Solution1().subArraySum(arr,s))