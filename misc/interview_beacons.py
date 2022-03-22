"""Write a function that simulates rolling an unfair N sided die.

Args:
    weights: an list of probabilities for rolling each side of the die, e.g.
    [.1, .2, .3, .4] = p(side 1) = .1, p(side 2) = .2, etc...
    Other examples:
    [.3, .05, .1, .55]
    [.9, .1]
    [.95, .05]
    Only constraint is that the sum(weights) = 1
    Assume arbitrary length of weights

Returns:
    a side number (starting at 1)

example:
[.95, .05]
> approach #1:
1. generate rand num between 0-1
2. if sum(a[0]..a[j]) < num < sum(a[0]..a[i]) => a[i]

[.3, .05, .1, .55]

"""

from random import random


def roll_unfair_die(weights):
    num = random()
    for i in range(len(weights)):
        if sum([w for idx, w in enumerate(weights) if idx < i]) <= num < sum(
            [w for idx, w in enumerate(weights) if idx <= i]):
            return i + 1


def roll_unfair_die_cumulative(cumulative_weights):
    """
    
    weights (list): [.3, .05, .1, .55]

    cumulative_weights (list): [.3, .35, .45, 1]
    """
    num = random()
    for i in range(len(cumulative_weights)):
        if (cumulative_weights[i - 1] if i > 0 else 0) <= num < cumulative_weights[i]:
            return i + 1


from collections import defaultdict


def test_unfair_die(n, test_arr):
    results = defaultdict(int)
    for i in range(n):
        result = roll_unfair_die(test_arr)
        results[result] += 1
    return results


def test_unfair_die_cumulative(n, test_arr):
    results = defaultdict(int)
    for i in range(n):
        result = roll_unfair_die_cumulative(test_arr)
        results[result] += 1
    return results


print(test_unfair_die(10000, [.3, .05, .1, .55]))
print(test_unfair_die_cumulative(10000, [.3, .35, .45, 1]))
