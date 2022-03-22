"""Sliding Window Median (Hard)
# approach #1: keep frequency counter and use histogram pattern to calculate median <-- (wrong: only works if element of array is restricted among few values)
# approach #2: keep min and max balanced heaps, extract one of each for even k and "remainder" num for odd k. O(n.log k)

example:
arr = [1,3,-1,-3,5,3,6,7], k = 3

[1,3,-1,-3,5,3,6,7]
 ^    ^ 1
[1,3,-1,-3,5,3,6,7]
   ^     ^ -1
[1,3,-1,-3,5,3,6,7]
      ^    ^ -1
[1,3,-1,-3,5,3,6,7]
         ^   ^ 3
[1,3,-1,-3,5,3,6,7]
           ^   ^ 5
[1,3,-1,-3,5,3,6,7]
             ^   ^ 6

output: [1,-1,-1,3,5,6]


solution from leetcode:
https://leetcode.com/problems/sliding-window-median/discuss/262689/Python-Small-and-Large-Heaps

def medianSlidingWindow(nums, k):
	small, large = [], []
	for i, x in enumerate(nums[:k]): 
		heapq.heappush(small, (-x,i))
	for _ in range(k-(k>>1)): 
		move(small, large)
	ans = [get_med(small, large, k)]
	for i, x in enumerate(nums[k:]):
		if x >= large[0][0]:
			heapq.heappush(large, (x, i+k))
			if nums[i] <= large[0][0]: 
				move(large, small)
		else:
			heapq.heappush(small, (-x, i+k))
			if nums[i] >= large[0][0]: 
				move(small, large)
		while small and small[0][1] <= i: 
			heapq.heappop(small)
		while large and large[0][1] <= i: 
			heapq.heappop(large)
		ans.append(get_med(small, large, k))
	return ans

def move(h1, h2):
	x, i = heapq.heappop(h1)
	heapq.heappush(h2, (-x, i))
	
def get_med(h1, h2, k):
	return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.

https://leetcode.com/problems/sliding-window-median/
"""

from collections import Counter

def median_from_histogram(freq, k):
    """
    k % 2 == 0 => return 2 middle nums / 2
    k % 2 != 0 => return single middle num

    """
    half = k // 2
    middle_nums = []
    acc = 0
    for num, f in freq.items():
        acc += f
        if acc >= half:
            middle_nums.append(num)
        

def sliding_window_median(arr, k):
    freq = Counter(arr[:k])
    result = [median_from_histogram(freq, k)]
    for i in range(k, len(arr)):
        freq[arr[i-k]] -= 1
        freq[arr[i]] += 1
        result.append(median_from_histogram(freq, k))
    return result





"""
solution: https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find

from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
"""



"""
solution: https://www.geeksforgeeks.org/find-subarray-with-given-sum/

"""

def subArraySum(arr, sum):     
    curr_sum = 0
    j = 0
    for i in range(len(arr)):
        while curr_sum > sum and j < i:
            curr_sum = curr_sum - arr[j]
            j += 1
        if curr_sum == sum:
            return (j,i)
        curr_sum = curr_sum + arr[i]
 
    print ("No subarray found")
    return 0
 