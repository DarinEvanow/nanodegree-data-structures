# Square Root

## Summary

For this problem we are implementing a function to find the floored square root of a number.
For example, 27 is not a perfect square. The closest square root would be the square root of 25, which
is 5.

## Implementation

The implementation involves doing a binary search for the square root. Similar to searching
for a number in an array, we set the boundaries as 1 and the number, and then find the midpoint using
integer division. If the midpoint squared is the number, it's a perfect square and we have our solution.
If the midpoint squared is less than the number, we move the starting boundary up and repeat the process.
If the midpoint squared is larger than the number, we move the end boundary down and repeat the process.

# Time and Space Analysis
This algorithm has a runtime of O(log n) as it is just a modified binary search. It has a space complexity