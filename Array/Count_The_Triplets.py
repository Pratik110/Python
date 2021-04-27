Link = "https://practice.geeksforgeeks.org/problems/count-the-triplets4615/1"
Description = "Given an array of distinct integers. The task is to count all" \
              "the triplets such that sum of two elements equals the third element."
Example = "N = 4" \
          "arr[] = {1, 5, 3, 2}" \
          "Output: 2" \
          "Explanation: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5"
arr = [1, 5, 3, 2]
class Solution1:
    def countTriplet(self,arr):
        l = len(arr)
        maxm = 0
        for i in arr:
            if i > maxm:
                maxm = i
        index_arr = [0] * (maxm*2 +1)
        for i in arr:
            index_arr[i] = 1
        count = 0
        for i in range(l):
            for j in range(i+1,l):
                if index_arr[arr[i]+arr[j]] == 1:
                    count+=1
        return count
print("The number of triplets in array {} is".format(arr),Solution1().countTriplet(arr))