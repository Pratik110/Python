Link1 = "https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/"
Link2 = "https://www.techiedelight.com/inplace-merge-two-sorted-arrays/"
Description = "Given two sorted arrays, we need to merge them in O((n+m)*log(n+m)) time with O(1) extra " \
              "space into a sorted array, when n is the size of the first array, and m is the size of the" \
              "second array."
Example = "Input: " \
          "ar1[] = {1, 5, 9, 10, 15, 20};" \
          "ar2[] = {2, 3, 8, 13};" \
          "Output: " \
          "ar1[] = {1, 2, 3, 5, 8, 9}" \
          "ar2[] = {10, 13, 15, 20}"
# Gap Algorithm
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
import math
class Solution:
    def mergeSortedArray(self,ar1,ar2):
        l1 = len(ar1)
        l2 = len(ar2)
        ar1+=ar2
        l = len(ar1)
        gap = math.ceil(l/2)
        while gap>0:
            i = 0
            j = i+gap
            while j < l:
                if ar1[i] > ar1[j]:
                    temp = ar1[i]
                    ar1[i] = ar1[j]
                    ar1[j] = temp
                i+=1
                j+=1
            gap//=2
        whole_array = ar1
        ar1 = whole_array[:l1]
        ar2 = whole_array[l1:]
        return ar1, ar2
print(*Solution().mergeSortedArray(ar1,ar2))