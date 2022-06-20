# Data Structures and Algorithms

## Language: `Python`
## Challenge Type: `Code Challenge / Algorithm`


# linked-list-zip
## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/linked_list_zip/linked_list_zip.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_linked_list_zip.py)

## Challenge08

[ two linked lists as inputs, 
and we want to merge them together so that they alternate between values. 
If one list is longer than the other, 
start adding the extra values in order from the linked list that is longer than the other. 
Return a reference to head of zipped list.


## Whiteboard Process
[WhiteBoard](cc08.jpg)

## Approach & Efficiency
Cache the head of both lists. While those both have values, 
cache the next node for each in separate variables. 
Set the next of the first list's first value to the second list's first value and so on, 
until one list runs out of nodes. In that case, 
the original sequence of the list with more nodes is continued until the end is reached.
Utilized existing methods in the LinkedList class to test output. Time: O(n) Space: O(1).

