# Rearrange Array Elements

## Summary

For this problem we are trying to take an array of numbers and arrange them into two distinct integers that,
when added together, give the largest possible number.

## Implementation

The implementation involves constructing a max-heap, and then constructing the two integers by
popping the top element off the heap, and alternating which integer we append it to. This pattern works
because conceptually we construct the largest number possible by ensuring the largest single
digit integers go onto the front of our constructed multi-digit integers. 

## Time and Space Analysis
This algorithm has a runtime of O(n logn) since we will first need to iterate over the list in order to
construct the heap, and each time we add an element to the list it has a runtime of O(log n). For the space
complexity, since we also end up storing every element in the list in the heap, we have a space complexity
of O(n) as well. Since we are only creating two numbers, we have a constant space complexity for the storage
of the results, which we can remove from our final analysis.