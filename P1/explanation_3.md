# Huffman Coding

## Summary

Huffman Coding is a way of compressing data. The way this is done is by first taking a piece of data,
in this case of string, and finding out the frequency of each data item. From there, we can assign
codes to each value, with smaller codes being assigned to the values that appear most frequently.

## Implementation

### Compression

Our implementation is broken into two main parts: compression and decompression. The majority of the
work happens in the compression algorithm, which I will go into first.

The compression algorith itself if broken into 5 parts.

1. Finding out the frequency of each character in our string: This is done by looping over the
text and populating a dict. Each character we haven't seen yet gets added to the dict as a key with
a value of 1. Characters we have seen get their associated values incremented by one. At the end,
we will have a dict where each character is a key that corresponds to their frequency in the string.
This takes O(n) time, as we need to loop through the entire string.

2. Creating a tree with these frequencies: Here we simply loop over our dictionary and construct
a priority queue with the values from our dict. We must loop over all the elements in our dict, 
so this part takes O(n) time. Then, we can start making a tree out of them by taking the two
lowest priority items from our queue, and inserting them into the tree, with their parent node
being the sum of their frequencies. Every time we want to insert an element from the queue into
the tree, we must navigate the tree, which takes O(logn) time. Therefore, between iterating over
the queue and navigating the tree, this part of the algorithm takes a combined time of O(nlogn).

4. Creating the codes: Now we traverse the tree. Anytime we traverse to the left, we add a "0"
to our code, and anytime we traverse to the right, we add a "1". Once we hit a leaf, whatever
code we currently have is associated with that character in our node. Traversing the entire tree
in this manner to assign all the codes take O(n).

5. Converting our text into the codes: Now we can loop over our original string, and for each
character in our original string, append it's associated code to our compressed string. Once again,
looping over our string takes O(n).

At the end of this we will have our compressed string. The largest chunk of time is in creating
the tree with all of the frequencies, which gives us the time of our algorithm at O(nlogn).

The space complexity will be O(n) + O(k), where n is the length of the string, and k is the size
of the tree created during the encoding process.

### Decompression

Decompressing the code is simply a matter of iterating over our compressed string, looking for
associated values in our mapping as we go. Since we are iterating over a string, it takes
O(n).