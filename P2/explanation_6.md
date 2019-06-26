# Max and Min in a Unsorted Array

## Summary

For this problem we want to iterate over a list of integers, and find the minimum and maximum elements.

## Implementation

The implementation for this problem is pretty straight forward. We begin by setting minimum and maximum
variables to the value at the beginning of the list. Then, we iterate over the elements in the list, and, for
each element in the list, we compare against the minimum and the maximum. If the element is less than
the current minimum, we set it as the new minimum. If the element is greater than the current maximum,
we set it as the new maximum.

## Time and Space Analysis
This algorithm has a runtime of O(n) since we must iterate over every element in the list. It also has
a space complexity of O(n), as we only need to store the list itself, and two placeholder variables
for the minimum and maximum.