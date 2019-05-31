# Union and Intersection

## Summary

Two extremely common set functions are union and intersection. Union creates a new set that contains
all of the elements that are found in either of the sets being passed into the union function.
Intersection creates a new of all the elements that are found in both of the sets passed into the
intersection function.

## Implementation

### Union
For our union implementation, we were given the criteria of being passed in two linked lists and
returning a linked list. To implement the union function, we simply loop over each of our lists
and check to see if the element in that list has already been added to our union. Since for each
element in the lists passed in we must also search through the union list, our union function
has a runtime of O(n^2).

### Intersection
The intersection implementation follows a similar logic as the union function, with some small
differences. First, we want to find the largest list, as we will want to use that to dictate
how many times we iterate. Then, we iterate through the larger list, checking to see if
the element also exists in our smaller (or equal size) list. If it does, we also check to see if
it exists in the intersection list we are constructing. If it does not, we add it into the
intersection list. Since again we are doing nested looping, our intersection function has a
runtime of O(n^2).