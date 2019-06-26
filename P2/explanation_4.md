# Dutch National Flag Problem

## Summary

For this problem we want to sort an array containing the integers 0, 1, and 2 in a single traversal, without
the use of any sorting methods provided by Python.

## Implementation

The implementation involves iterating through the array while maintaining three pointers, each one
corresponding to the location of an integer. What we do is move the pointer where we are going to put the 
1's forward. Each time that pointer comes across a 0, we swap it with the value of the 0 pointer, and increment
the 0 and 1 pointers. On the other hand, if the 1 pointer encounters a 2, we swap that with the 2 pointer, and
decrement the 2 pointer. This continues until all the 0's and 2's are built up on their ends, which leaves
the 1's in the correct place.

## Time and Space Analysis
This algorithm has a runtime of O(n) since we are traversing the list only once, and a space complexity of O(n)
since we do all of the sorting on the array itself without constructing any additional data structures to hold
intermediary values.