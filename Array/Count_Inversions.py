Link = "https://www.geeksforgeeks.org/counting-inversions/"
Description = "Inversion Count for an array indicates – how far (or close)" \
              "the array is from being sorted. If the array is already sorted," \
              "then the inversion count is 0, but if the array is sorted in the" \
              "reverse order, the inversion count is the maximum. Formally speaking" \
              ", two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j "
Example = "Input: arr[] = {8, 4, 2, 1}" \
          "Output: 6" \
          "" \
          "Explanation: Given array has six inversions:" \
          "(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1)."

arr = [8, 4, 2, 1]
# Approach 1 Brute Force Approach
class Solution1:
    def getInvCount(self,arr):
        l = len(arr)
        count = 0
        for i in range(l):
            for j in range(i,l):
                if arr[i] > arr[j]:
                    count+=1
        return  count
print("The number of inversions in {} is".format(arr),Solution1().getInvCount(arr))

# Approach 2
class Solution2:
    def getInvCount(self,arr):
        pass
        return  count
print("The number of inversions in {} is".format(arr),Solution2().getInvCount(arr))