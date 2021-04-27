Link = "https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1"
Description = "Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order." \
              "Merge them in sorted order without using any extra space. Modify arr1 so that it" \
              "contains the first N elements and modify arr2 so that it contains the last M elements."
Examples = "Input: " \
           "n = 4, arr1[] = [1 3 5 7] " \
           "m = 5, arr2[] = [0 2 6 8 9]" \
           "Output: " \
           "arr1[] = [0 1 2 3]" \
           "arr2[] = [5 6 7 8 9]" \
           "Explanation: After merging the two non-decreasing arrays, we get, 0 1 2 3 5 6 7 8 9."

arr1 = [1,36,39,105,146,154,168,170,204,206,217,219,225,227,272,282,293,300,312,323,328,328,334,335,359,370,383,392,395,396,403,413,422,437,443,448,462,463,465,479,492,496]
arr2 = [7,22,30,36,38,38,39,41,42,48,49,83,85,102,107,116,119,124,127,130,140,142,145,149,159,163,165,174,174,191,205,212,224,230,242,246,254,257,258,265,279,289,306,307,309,317,324,334,341,343,351,360,369,371,377,387,391,394,430,431,432,440,443,445,447,455,467,478]
n = 42
m = 68
# Approach 1
class Solution1:
    def merge(self,arr1,arr2,n,m):
        i = 0
        while i < n:
            if arr1[i] > arr2[0]:
                arr1[i],arr2[0] = arr2[0],arr1[i]
                arr2.sort()
            i+=1
        arr1+=arr2
        return arr1
print(Solution1().merge(arr1, arr2, n, m))
