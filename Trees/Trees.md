# Trees

## Language: `Python`
## Challenge Type: ` Code Challenge / New Implementation`


## Challenge Binary Tree and BST

## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/Trees/Trees.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_Trees.py)


## Challenge

Create three classes, Node, BinaryTree, and BinarySearchTree. Using test-driven development, implement/test the following features:

1. Can successfully instantiate an empty tree
2. Can successfully instantiate a tree with a single root node
3. Can successfully add a left child and right child to a single root node
4. Can successfully return a collection from a preorder traversal
5. Can successfully return a collection from an inorder traversal
6. Can successfully return a collection from a postorder traversal
7. Returns true	false for the contains method, given an existing or non-existing node value

## Whiteboard Process
NO WHITEBOARD FOR THIS CODE CHALLENGE.

## Approach & Efficiency
We tried to keep our code as simple as possible to the best performance by reducing space/Time complexity
so we end with the following

Big O:
1. Time complexity => O(N) for both adding a new node and searching for a specific node using recursive.
2. Space complexity => O(N) for a node addition only, and O(1) for the contains method


## API 
- declare a TNode class that has properties for the value stored in the node, the left child node, and the right child node
- declare a BinaryTree class 
- declare a method for each of the depth first traversals called preOrder, inOrder, and postOrder  array which returns an array of the values, ordered appropriately  using recursive and if-else statment to loop through the tree to return in the end an array as output (The array we declare it as empty array in each method )
- declare a BinarySearchTree class
- declare a method named add that accepts an argument, and adds a new node with that value in the correct location in the binary search tree using while loop.(by understanding the concept of binery search)
- declare a method named contains that accepts an argument, and returns a boolean (True $ False) indicating whether or not the value is in the tree at least once.