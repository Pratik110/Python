Link = "https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1"
Description = "Given an array of size N-1 such that it only contains distinct" \
              "integers in the range of 1 to N. Find the missing element."
Example = "Input:" \
          "N = 5" \
          "A[] = {1,2,3,5}" \
          "Output: 4"

arr = [1,2,3,4,5,6,7,8]
# Approach 1 Sort and find with time complexity of sorting + n
class Solution1:
    def MissingNumber(self,arr,l):
        arr.sort()
        for i in range(l):
            if i == l-1:
                return l
            if i+1 != arr[i]:
                return i+1
print("The missing element in array {} is".format(arr),Solution1().MissingNumber(arr,9))

# Approach 2 , an efficient approach to do the same in a time complexity of n with 1 pass
# In this approach we'll be using the hashmap

class Solution2:
    def MissingNumber(self,array,n):
        hashmap = [0]*n
        for i in array:
            hashmap[i-1] = 1
        for i in range(n):
            if hashmap[i] == 0:
                return i+1
print("The missing element in array {} is".format(arr),Solution2().MissingNumber(arr,9))