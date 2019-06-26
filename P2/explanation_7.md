# HTTPRouter using a Trie

## Summary

For this problem we want to use a trie to replicate the functionality of an HTTP router. For example,
we want to have the trie be able to store routes, such as "/home/about/me", along with a value
that would indicate what to do once we reached an end route that can take requests.

## Implementation

The implementation of this problem is similar to our implementation of autocorrect. We use a trie
structure to maintain a series of nodes. Each node represents a part of a path, with a list of children
that represent the paths that follow, and the node at the end of the path will have a handler as well.
When adding a new path we simply split the path into it's parts, so that "/home/about/me" would split into
["home, "about", "me"], and then add it into our trie along with a handler so that in the trie it would
be represented as (root, None) -> ("home", None) -> ("about", None) -> ("me", "About Me handler"). Then, when
searching for elements we can simply pass in a path, and try to traverse the list of nodes using the elements
in the given path as keys. If the path exists and leads to a handler, we can return that handler.

## Time and Space Analysis
Similar to problem five, this algorithm has a runtime of O(n) since when we are constructing the trie, 
we will need to iterate over each element in the given path and construct the trie while traversing the path. 
There is a similar runtime for searching the trie for the handler, as we do a similar process of iterating
the path until we get to the node we are looking for. The space complexity of the tree is also O(n), 
as it is dependent on how long the path is that we are being passed in, and we only need to 
construct one node for each part of the path.