"""
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]

https://leetcode.com/discuss/interview-question/579606/count-contiguous-subarrays

-- O(n) solution in Java --
counts from left to right contiguous subarrays then reverse
 int[] countSubarrays(int[] arr) {
    Stack<Integer> stack = new Stack<>();
    int[] ans = new int[arr.length];
    for(int i = 0; i < arr.length; i++) {
      while(!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
        ans[i] += ans[stack.pop()];
      }
      stack.push(i);
      ans[i]++;
    }
     stack.clear();
    int[] temp = new int[arr.length];
     for(int i = arr.length - 1; i >= 0; i--) {
      while(!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
        int idx = stack.pop();
        ans[i] += temp[idx];
        temp[i] += temp[idx];
      }
      stack.push(i);
      temp[i]++;
    }
    return ans;
  }
--
arr = [3, 4, 1, 6, 2]
ans = [0, 0, 0, 0, 0]
i==0
stack = [3]
ans = [1, 0, 0, 0, 0]
i==1
stack = [4]
ans = [1, 2, 0, 0, 0]
i==2
stack = [4, 1]
ans = [1, 2, 1, 0, 0]
i==3
stack = [6]
ans = [1, 2, 1, 4, 0]
i==4
stack = [6, 2]
ans = [1, 2, 1, 4, 1]
-- clears stack, starts over right to left and adds both answers
"""

def onesided_count_subarrays(arr, order='ltr'):
    ans = [0] * len(arr)
    stack = []
    iterable = range(len(arr)) if order == 'ltr' else range(len(arr) - 1, -1, -1)
    for i in iterable:
        while len(stack) > 0 and arr[stack[-1]] < arr[i]:
            ans[i] += ans[stack.pop()]
        stack.append(i)
        ans[i] += 1
    return ans

def count_subarrays(arr):
  left = onesided_count_subarrays(arr)
  right = onesided_count_subarrays(arr, 'rtl')
  return [v + right[i] - 1 for (i, v) in enumerate(left)]


"""
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
"""

from collections import defaultdict
from email.policy import default
def numberOfWays(arr, k):
    frequency = defaultdict(int)
    ans = 0
    for i in range(len(arr)):
        frequency[arr[i]] += 1
    for i in range(len(arr)):
        ans += frequency[k - arr[i]]
        if k / 2 == arr[i]: ans -= 1
    return ans / 2


"""
Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.
Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.
Example 1
n = 2
arr = [2, 1]
output = [2, 2]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is Student 2.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is Student 1.
Pass 2:
Student 1 signs Student 2's yearbook. Then they pass it to the student at arr[0], which is Student 2.
Student 2 signs Student 1's yearbook. Then they pass it to the student at arr[1], which is Student 1.
Pass 3:
Both students now hold their own yearbook, so the process is complete.
Each student received 2 signatures.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is themself, Student 1.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is themself, Student 2.
Pass 2:
Both students now hold their own yearbook, so the process is complete.
Each student received 1 signature.

other examples:
[1,2,3,4] => [1,1,1,1]
[1,3,2,4] => [1,2,2,1]
[4,1,2,3] => [4,4,4,4]
[3,4,1,2] => [2,2,2,2]
[2,3,4,1] => [4,4,4,4]
[3,2,4,1] => [3,1,3,3]
[5,2,4,3,1] => [2,1,2,2,2]
5 -> 1 -> 5 => 2
2 -> 2      => 1
4 -> 3 -> 4 => 2
3 -> 4 -> 3 => 2
1 -> 5 -> 1 => 2

https://leetcode.com/discuss/interview-question/614096/facebook-interview-preparation-question-passing-yearbooks
"""

# # An attempt at a more OOP solution
# class StudentYearClass:
#     def __init__(self):
#         self.members: list[Student] = []
#     def get(self, num):
#         if num > len(self.members) - 1:
#             return Student(num)
#         else:
#             return self.members[num - 1]

# class Student:
#     def __init__(self, number, yearbook=None):
#         self.yearbook = yearbook or Yearbook(self)
#         self.number = number

# class Yearbook:
#     def __init__(self, owner):
#         self.owner = owner
#         self.signatures = 0
#     def sign(self):
#         self.signatures += 1

# def findSignatureCounts(arr):
#     students = StudentYearClass()
#     for i in range(len(arr)):
#         curr_student = students.get(i + 1)
#         next_student = students.get(arr[i])
#         while curr_student.yearbook.owner != next_student:
#             curr_student.yearbook.sign()
#             next_student.yearbook = curr_student.yearbook
#             # pending .....

# # Another attempt -- almost
# from collections import defaultdict
# def findSignatureCounts(arr):
#     yearbooks = {} # { [student/owner]: { 'signatures': int, 'root': int } }
#     for i in range(len(arr)):
#         student = arr[i]
#         if student in yearbooks: continue

#         yearbooks[student] = { 'signatures': 1, 'root': student }
#         next_i = student - 1
#         while next_i != i:
#             yearbooks[student]['signatures'] += 1
#             yearbooks[arr[next_i]] = { 'root': student }
#             next_i = arr[next_i] - 1

#     return [v['signatures'] if 'signatures' in v else yearbooks[v['root']]['signatures'] for k,v in yearbooks.items()]

def findSignatureCounts(arr):
    visited = set()
    signatures = [0] * len(arr)
    root_idx = [-1] * len(arr)

    for i in range(len(arr)):
        node = arr[i]
        if node in visited: continue
        visited.add(node)

        # consider the current node to be the root of a cycle, and traverse back to itself
        signatures[i] = 1
        next_i = node - 1
        while next_i != i:
            signatures[i] += 1
            root_idx[next_i] = i
            visited.add(arr[next_i])
            next_i = arr[next_i] - 1

    # return the signature counts of the root nodes, and the referenced root node counts of traversed nodes
    for i in range(len(arr)):
        if root_idx[i] != -1:
            signatures[i] = signatures[root_idx[i]]
    return signatures

tests = [
    ([1,2,3,4],[1,1,1,1]),
    ([1,3,2,4],[1,2,2,1]),
    ([4,1,2,3],[4,4,4,4]),
    ([3,4,1,2],[2,2,2,2]),
    ([2,3,4,1],[4,4,4,4]),
    ([3,2,4,1],[3,1,3,3]),
    ([5,2,4,3,1],[2,1,2,2,2]),
    ([5,2,4,3,6,1],[3,1,2,2,3,3])
]
"""
[5,2,4,3,6,1]
5-6-1-5
2-2
4-3-4
3-4-3
6-1-5-6
1-5-6-1
=> [3,1,2,2,3,3]
"""

print('-- Testing findSignatureCounts ---')
for input, output in tests:
    print(f"{input} <<< input\n{findSignatureCounts(input)} >>> output eq?\n{output} {'✅' if findSignatureCounts(input) == output else '❌'}")
print('-- EOF Testing findSignatureCounts ---\n')