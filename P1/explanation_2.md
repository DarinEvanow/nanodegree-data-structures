# File Recursion

## Summary

The goal for this problem is to navigate a file tree in search for any files that end with the
".c" file extension.

## Implementation

The implementation I went with is a fairly simple recursive approach. Given a path, we display all
of the files and directories. If any of them have the file extension we want, we add the complete
path to the file to a list of results. For any directory in the path, we repeat the above
logic until there are no more directories or files to iterate over. The runtime of this algorithm
is O(n), since each additional file or directory would just add another step to iterate over. The space
complexity of the problem is also O(n), as we will need to populate a list of our results, which will
scale linearly with the size of our input.