# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!

# // Given an array of integers, find any one local minimum from the array.
#     //    // A local minimum is defined as an integer in the array that is less to its neighbors.
#     //    // {5, 12, 9, 10, 6, 13, 14}

"""
input: list[int]
-inf < n < inf
output: int

> approach #1: iterate through array with 3 pointers - O(n)
1. check first element and second
2. if not local_min move both pointers forward
> approach #2: 

example:
[5, 12, 9, 10, 6, 13, 14] // first
 
[12, 9, 10, 6, 13, 14] // second

[14, 13, 12] // last
// negative elements
// considered equal numbers
// considered all invalid input
// test environment
// 


"""

def find_local_minimum(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] < arr[i+1]: return arr[i]
        if i == len(arr) - 1 and arr[i-1] > arr[i]: return arr[i]
        if i < len(arr) and arr[i-1] > arr[i] < arr[i+1]: return arr[i]
        
    
# // We have a game in which consecutive duplicate pieces of the same type cancel each other out and remaining pieces slide in, until no more pieces can be removed.
#     //
#     // Given a board, represented by a string, return the final state of the board after playing the game.
#     //
#     //Example:
#     //Input: "abbba"
#     //Output: "" ("abbba" => "aa" => "")

"""
"aabbccdd" -> ""
"aabbcdd" -> "c"
"aabbcddc" -> ""
"abcdef" -> "abcdef"

input: string
output: string

example:
"aacbbcddc"
{a:2,b:2,c:1,d:2,c:1}

"aacbcefgddc"
    ^       
c 1, b 1, c1

> approach #1: frequency map

> approach #2: iterate string mapping frequencies


"""

def play_game(s):
    for i, letter in enumerate(s[:-1]):
        while s[i+1] == s[i]:

    
    
# solution https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/
    












