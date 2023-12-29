# Splay binary search tree on Python
A simple fully-working realization of Splay binary search tree as a class on Python programming language.

_This realization was originally created in march 2022._
## What is a Splay-tree
A splay tree is a binary search tree with the additional property that recently accessed elements are quick to access again. Like self-balancing binary search trees, a splay tree performs basic operations such as insertion, look-up and removal in O(log n) amortized time. For random access patterns drawn from a non-uniform random distribution, their amortized time can be faster than logarithmic, proportional to the entropy of the access pattern. For many patterns of non-random operations, also, splay trees can take better than logarithmic time, without requiring advance knowledge of the pattern.
## Operations in a Splay-tree
### Splay
An operation that bring the accesed node of the tree to its root.
### Zig step (right rotation of the tree)
A suboperation that rotates a subtree of the Splay-tree right.
### Zag step (left rotation of the tree)
A suboperation that rotates a subtree of the Splay-tree left.
### Insertion
An operation that inserts a node into the Splay-tree.
### Deletion
An operation that deletes a node from the Splay-tree.
## Methods of the Splay-tree class
All of the operations described above are realized as methods of the Splay-tree class. In adddition to that, all of the functions of a Python dictionary are among the methods of this class.
