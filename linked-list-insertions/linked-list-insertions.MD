# Data Structures and Algorithms

## Language: `Python`
## Challenge Type: `Extending an Implementation`


# linked list
## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/linked_list/linked_list.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_linked_list.py)

## Challenge06

Using test-driven development, create functions that append an element to the end of a linked list, before a specified value, and after a specified value.

## Whiteboard Process
[WhiteBoard](cc06%20v1.1.jpg)

## Approach & Efficiency
Node and LinkedList classes have already been created and tested. 
After writing each test, we went in to write the actual implementation function.
After that, we ran the tests to make sure each function produces the expected values. 
Inserting at the head of the linked list is O(1) because it will always take the same amount of time.
Inserting anywhere else in a linked list will be O(n) time because time is dependent on how many elements we need to traverse through. 
Space will be O(1) because the space required by the algorithm is constant.

