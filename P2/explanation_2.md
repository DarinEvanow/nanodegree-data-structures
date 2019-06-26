# Rotated Array Search

## Summary

For this function we are trying to search for an element in a rotated array. A array is rotated when it is
in order, but when all of the elements are shifted to the right, with the element that is at the end of the
list moving to the beginning of the list each time it is shifted. The goal is to do this in less than
linear time.

## Implementation

The implementation involves finding a pivot point, and then doing a binary search on each side of the pivot.
In this case we want the pivot point to be where the list was rotated.

## Time and Space Analysis
This algorithm has a runtime of O(log n) as it is just a modified binary search. It has a space complexity
of O(log n) since we will need to hold the recursive calls in the stack.