
# ----- Merge Sort: Counting Inversions - https://www.hackerrank.com/challenges/ctci-merge-sort/ -----
""" # solution from https://shareablecode.com/snippets/python-solution-for-hackerrank-problem-merge-sort-counting-inversions-5iG7-VTTw
def countInversions(array):
    cnt_inv = 0

    if len(array) <= 1:
        return array, 0

    ar_left, inv_left = countInversions(array[:int(len(array)/2)])
    ar_right, inv_right = countInversions(array[int(len(array)/2):])

    ar_merged = []
    i = j = 0
    len_left = len(ar_left)
    len_right = len(ar_right)
    
    for k in range(len(array) - 1):
        if i == len_left or j == len_right:
            break

        if ar_left[i] <= ar_right[j]:
            ar_merged.append(ar_left[i])
            i += 1
        else:
            ar_merged.append(ar_right[j])
            j += 1
            cnt_inv += len_left - i

    ar_merged += ar_left[i:]
    ar_merged += ar_right[j:]
    return ar_merged, cnt_inv + inv_left + inv_right
"""

""" # similar solution from https://allhackerranksolutions.blogspot.com/2019/02/merge-sort-counting-inversions-hacker.html
# python2 - sorts in-place
def inversions(arr):
    n = len(arr)
    if n==1:
        return 0
    n1 = n/2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 <n1 and (i2>=n2 or arr1[i1]<=arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1 
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans
"""

# recursive merge sort
def inversions(array):
    swaps = 0
    if len(array) <= 1: return array, 0

    left, l_swaps = inversions(array[:int(len(array)/2)])
    right, r_swaps = inversions(array[int(len(array)/2):])

    merged = []
    i = j = 0    
    for _ in range(len(array) - 1):
        if i == len(left) or j == len(right): break

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            swaps += len(left) - i

    merged += left[i:]
    merged += right[j:]
    return merged, swaps + l_swaps + r_swaps