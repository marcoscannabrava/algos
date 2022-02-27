# # -------------------------------- Fraudulent Activity Notification --------------------------------
# was quite a struggle to get it right... :(
import os
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
        if i >= d and v >= 2 * get_median(freq, d):
            print('i,v:', (i,v))
            print('freq:', [(a,b) for (a,b )in enumerate(freq) if b > 0])
            print('median:', get_median(freq, d))
            count += 1
        freq[v] += 1
        if i >= d: freq[e[i-d]] -= 1
    return count


# # test #1
# test = open(f"{os.path.dirname(__file__)}/test.txt").readlines()
# d = int(test[0].replace('\n', '').split(' ')[-1])
# expenses = list(map(int, test[1].split(' ')))
# expect = 633
# print(d, expenses[10], '...', len(expenses))
# output = activityNotifications(expenses, d)
# print('expect: ', expect)
# print('output: ', output, f"{'✅' if output == expect else '❌'}")

# test #2
d = 3
expenses = [10,20,30,40,50]
expect = 1
output = activityNotifications(expenses, d)
print('expect: ', expect)
print('output: ', output, f"{'✅' if output == expect else '❌'}")