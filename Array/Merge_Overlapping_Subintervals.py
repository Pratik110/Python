Link = "https://leetcode.com/problems/merge-intervals/"
Description = "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals," \
              "and return an array of the non-overlapping intervals that cover all the intervals in the input."
Examples = "Input: intervals = [[1,3],[2,6],[8,10],[15,18]]" \
           "Output: [[1,6],[8,10],[15,18]]" \
           "Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]."
Note = "Ask the interviewer whether the array is sorted or not" \
       "In the input the array seems sorted but nowhere in the problem" \
       "it's mentioned that the inputs are sorted. By doing this you're making" \
       "sure that you're taking care of all the use cases."
#Approach 1
intervals1 = [[2,6],[1,3],[15,18],[8,10]]
intervals2 = [[1,4],[4,5]]
intervals3 = [[1,4],[0,0]]
class Solution:
    def merge(self,intervals):
        intervals = self.array_sort(intervals)
        l = len(intervals)
        output = [intervals[0]]
        for i in range(l):
            if output[-1][-1] >= intervals[i][0]:
                output[-1] = [output[-1][0], max(output[-1][-1],intervals[i][1])]
            else:
                output.append(intervals[i])
        print(output)
    def array_sort(self,elements):
        length = len(elements)
        l = len(elements)
        i = 0
        while i < length - 1:
            swapped = False
            j = 0
            while j < l - 1:
                if elements[j][0] > elements[j + 1][0]:
                    temp = elements[j]
                    elements[j] = elements[j + 1]
                    elements[j + 1] = temp
                    swapped = True
                j += 1
            if not swapped:
                break
            l -= 1
            i += 1
        return elements
Solution().merge(intervals1)
