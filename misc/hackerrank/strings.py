# -------------- Strings: Making Anagrams --------------
from collections import Counter
def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())

# ------------------- Sherlock and the Valid String -------------------
"""
'aabbccd' --> d = { 2: 3, 1: 1}
'aaabbbccd' --> d = { 2: 3, 1: 1}
"""
from collections import Counter
def isValid(s):
    d = Counter(Counter(s).values())
    if len(d)==1:
        return "YES"
    if len(d)>2:
        return "NO"
    if 1 in d.values() and (d[min(d.keys())]==1 or (max(d.keys()) - min(d.keys())==1)): # #wtf?
        return "YES"
    else:
        return "NO"


print(isValid(input()))

# ------------------- Special String Again ------------------- #medium ? #hard !!
""" solution from https://www.hackerrank.com/challenges/special-palindrome-again/forum
def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
		
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans
"""

# attempt 1
def substrCount(n, s):
    freq = []
    for i, l in enumerate(s):
        if i > 0 and s[i-1] == l: freq[i-1] = (l, freq[i-1][1] + 1)
        freq.append((l, 1))
    specials = 0
    for i, f in enumerate(freq[1:-1]):
        if f[1] == 1 and f[0] != freq[i-1][0] and freq[i-1] == freq[i+1]: specials += 1
    repeated_substrings = lambda x: sum(range(1,len(x)+1))
    return n + specials + sum([repeated_substrings(i[0]) for i in freq if i[1] > 1])
