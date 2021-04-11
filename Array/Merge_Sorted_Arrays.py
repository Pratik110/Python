Link = "https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/"
Description = "Given two sorted arrays, we need to merge them in O((n+m)*log(n+m)) time with O(1) extra " \
              "space into a sorted array, when n is the size of the first array, and m is the size of the" \
              "second array."
Example = "Input: " \
          "ar1[] = {1, 5, 9, 10, 15, 20};" \
          "ar2[] = {2, 3, 8, 13};" \
          "Output: " \
          "ar1[] = {1, 2, 3, 5, 8, 9}" \
          "ar2[] = {10, 13, 15, 20}"

ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
# Approach 1 -  Brute Force
class Solution1:
    def mergeSortedArray(self,ar1,ar2):
        l1 = len(ar1)
        ar3 = ar1+ar2
        ar3.sort()
        ar1 = ar3[:l1]
        ar2 = ar3[l1:]
        print(ar1, ar2)
Solution1().mergeSortedArray(ar1,ar2)

# Approach 2, In approach 1 we used another Array which is Array 3, but here we'll not use any extra space
class Solution2:
    def mergeSortedArray(self,ar1,ar2):
        l1 = len(ar1)
        for i in range(l1):
            if ar2[0] < ar1[i]:
                temp = ar1[i]
                ar1[i] = ar2[0]
                ar2[0] = temp
                ar2.sort()
        return ar1, ar2
print(*Solution2().mergeSortedArray(ar1,ar2))   # * collects/unpacks all the positional arguments/ elements in a tuple.
                                                # ** collects/unpacks all the keyword arguments/ elements in a dictionary.

Link = "https://www.techiedelight.com/inplace-merge-two-sorted-arrays/"