from collections import Counter, defaultdict

def count_anagrams(string):
    buckets = defaultdict(int)
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items()) # O(N) time key extract
            buckets[key] += 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count

# # TESTING
# tests=[
#     ('abba', 4),
#     ('abcd', 0),
#     ('kkkk', 10),
#     ('ifailuhkqq', 3)
# ]
# for i,o in tests:
#     print(f"{i} <<< input\n{o} == {count_anagrams(i)} {'✅' if count_anagrams(i) == o else '❌'}\n")
    
from collections import Counter
def count_triplets(arr, r):
    count = 0
    dict = Counter()
    dictPairs = Counter()

    for i in reversed(arr):
        if i*r in dictPairs:
            count += dictPairs[i*r]
        if i*r in dict:
            dictPairs[i] += dict[i*r]
        dict[i] += 1

    return count

# left and right counters pattern
def count_triplets_b(arr, r):
    a = Counter(arr)
    b = Counter()
    s = 0
    for i in arr:
        j = i//r
        k = i*r
        a[i]-=1
        if b[j] and a[k] and not i%r:
            s+=b[j]*a[k]
        b[i]+=1
    return s
"""
arr == [1,2,2,4*,8], r == 2
-
i == 4
j == 2
k == 8
a == { 1: 0, 2: 0, 4: 0 }
s == 2
b == { 1: 1, 2: 2 }
"""


# TESTING
tests=[
    (([1,2,2,4], 2), 2),
    (([1,5,5,25,125], 5), 4),
    (([1,4,16,64], 4), 2),
]
for i,o in tests:
    print(f"{i} <<< input\n{o} == {count_triplets(i[0], i[1])} {'✅' if count_triplets(i[0], i[1]) == o else '❌'}\n")


# Frequency Queries
from collections import defaultdict
def freqQuery(queries):
    data = defaultdict(int)
    freq = defaultdict(int)
    result = []
    for q in queries:
        if q[0] == 3:
            result.append(1 if freq[q[1]] > 0 else 0)
        else:
            if data[q[1]] in freq: freq[data[q[1]]] -= 1
            if q[0] == 1: data[q[1]] += 1
            if q[0] == 2 and data[q[1]] > 0: data[q[1]] -= 1
            freq[data[q[1]]] += 1
    return result
        