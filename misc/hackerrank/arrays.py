# -------------------------- Minimum Swaps --------------------------
import heapq
from timer import timer

@timer
def min_swaps(arr):
    """
    Given an array of integers, find the minimum number of swaps required to sort the array in ascending order.
    """
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            j = arr[i] - 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    return swaps


# From https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# by Dharan Aditya
@timer
def minSwapsGeek(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}

    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
 
@timer
def minSwapsLC(nums):
    keyToIndex = dict([(nums[i], i) for i in range(len(nums))])
    heap = nums[::]
    heapq.heapify(heap)

    swaps = 0
    for i in range(len(nums)):
        smallest = heapq.heappop(heap)

       # check if previous swappes luckily made the array sorted
        if nums[i] != smallest:
            currNum = nums[i] # needed to update the dic two lines below
            nums[i], nums[keyToIndex[smallest]] = nums[keyToIndex[smallest]], nums[i]
            keyToIndex[smallest], keyToIndex[currNum] = keyToIndex[currNum], keyToIndex[smallest]
            swaps += 1

    return swaps

# -------------------------- Array Manipulation --------------------------

# inefficient
def array_manipulation(n, queries):
    arr = [0] * n
    queries = sorted(queries, key = lambda x: x[0])
    for q in queries:
        for i in range(q[0], q[1] + 1):
            arr[i - 1] = arr[i - 1] + q[2]
    return max(arr)

# Optimized solution adapted from https://livecodestream.dev/challenge/array-manipulation-2/
def arrayManipulation(n, queries):
    acc = [0] * n
    for [a, b, k] in queries:
        acc[a - 1] += k
        if b < n: acc[b] -= k
    last = m = 0
    for i in range(n):
        last += acc[i]
        if (last > m):
            m = last
    return m


# -------------------------- Minimum Bribes --------------------------
# From https://www.hackerrank.com/challenges/new-year-chaos/forum
def min_bribes(q):
    moves = 0 
    q = [p-1 for p in q]
    for i, p in enumerate(q):
        if p - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1,0),i):
            if q[j] > p:
                moves += 1
    print(moves)

# -------------------------- Tests --------------------------
# arr = [1, 5, 4, 3, 2]
# print(min_swaps(arr))
# arr = [1, 5, 4, 3, 2]
# print(minSwapsGeek(arr))
# arr = [1, 5, 4, 3, 2]
# print(minSwapsLC(arr))

# queue = [1,2,5,3,4]
# min_bribes(queue)

# -------------------------- Fraudulent Activity Notifications --------------------------
# attempts 1,2,3 + links with hints/solutions
"""
use counting sort + queue? study counting sort
https://www.interviewcake.com/concept/java/counting-sort
https://en.wikipedia.org/wiki/Counting_sort
https://www.programiz.com/dsa/counting-sort
# inefficient when d is large
import bisect
# from statistics import median
class RunningMedianBisect:
    def __init__(self, array):
        self.sorted_set = []
        self.data = array
    def calculate(self, n, curr_idx):
        bisect.insort(self.sorted_set, self.data[curr_idx])
        if curr_idx >= n:
            if curr_idx > n:
                del self.sorted_set[bisect.bisect_left(self.sorted_set, self.data[curr_idx-n-1])]
            if n % 2 == 0:
                median = (self.sorted_set[n//2-1] + self.sorted_set[n//2]) / 2
            else:
                median = self.sorted_set[n//2]
            return median
        return False

# using a frequency dict -- not working anymore, see previous commit
from collections import defaultdict
class RunningMedianFreqHist:
    def __init__(self, array, n):
        self.freq = defaultdict(int)
        for i in array[:n-1]: self.freq[i] += 1
        self.data = array
        self.n = n
    def calculate(self, curr_idx):
        print(curr_idx, self.data[curr_idx])
        self.freq[self.data[curr_idx]] += 1
        if curr_idx >= self.n:
            if curr_idx > self.n: self.freq[self.data[curr_idx - self.n - 1]] -= 1
            total = 0
            for i in range(201):
                total += self.freq[i]
                if total > n//2:
                    if self.n % 2 == 0:
                        print(i + 0.5); return i + 0.5
                    else:
                        print(i); return i
        else:
            return False

def activityNotifications(expenditure, d):
    median = RunningMedianFreqHist(expenditure, d)
    notices = 0
    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * median.calculate(i):
            notices += 1
            print('notice!')
    return notices
"""

# solution from https://www.thepoorcoder.com/hackerrank-fraudulent-activity-notifications-solution/
"""
def get_limit(f,d):
    count = 0 
    m1,m2 = (d//2,d//2+1)
    m = []
    for i,j in enumerate(f):
        count+=j
        if not m and m1<=count:
            m.append(i)
        if m2<=count:
            m.append(i)
            break
    return m[-1]*2 if d%2 else sum(m)

def activityNotifications(e, n, d):
    f = [0]*201
    count = 0
    for i in e[:d]:
        f[i]+=1
    for i,v in enumerate(e[d:]):
        limit = get_limit(f,d)
        if v>=limit:
            count+=1
        f[v]+=1
        f[e[i]]-=1

    return count
n,d = map(int,input().split())
e = list(map(int,input().split()))
print(activityNotifications(e, n, d))
"""

# attempt 4
"""
def get_median(f, d):
    count = 0
    sorted_days = []
    for i in range(len(f)):
        while f[i]: # WRONG - this makes the time complexity shoot up
            count += 1
            f[i] -= 1
        sorted_days.append(i)
        if count == d // 2 + 1: break
    return sorted_days[-1] if d%2 else sum(sorted_days[-1], sorted_days[-2]) / 2

def activityNotifications(e,d):
    freq = [0] * 201
    count = 0
    for i, v in enumerate(e):
        freq[v] += 1
        if i == d: freq[e[i-d]] -= 1
        if i > d and v >= 2 * get_median(freq, d): count += 1
    return count
"""

# attempt 5
def get_median(freq, d):
    obs = 0
    middle = []
    for v, f in enumerate(freq):
        obs += f
        if obs >= d / 2 and len(middle) == 0: middle.append(v)
        if d%2 == 0 and obs > d // 2: middle.append(v)
        if (d%2 == 0 and len(middle) == 2) or (d%2 != 0 and len(middle) == 1): break
    return sum(middle)/2 if d%2 == 0 else middle[-1]

def activityNotifications(e,d):
    freq = [0] * 201
    count = 0
    for i, v in enumerate(e):
        if i >= d and v >= 2 * get_median(freq, d): count += 1
        freq[v] += 1
        if i >= d: freq[e[i-d]] -= 1
    return count
# -------------------- TESTING --------------------
# d = 5
# expenses = list(map(int, '2 3 4 2 3 6 8 4 5'.split(' '))) 
# expect = 2
d = 3
expenses = [10,20,30,40,50]
expect = 1
output = activityNotifications(expenses, d)
print('expect: ', expect)
print('output: ', output, f"{'✅' if output == expect else '❌'}")