# Data Structures and Algorithms

## Language: `Python`
## Challenge Type: `New Implementation`


# linked list
## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/linked_list/linked_list.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_linked_list.py)

## Challenge05
Create two classes, LinkedList and Node. Using test-driven development, implement/test the following features:
1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
For each of the features/requirements, I started by making a test that would prove that functionality. From there, I updated the Node and LinkedList classes to create the actual functionality that I would then test. After doing this for all of the features, I wrote docstrings to explain the purpose of each function that I constructed.

## API
Methods:
1. Node init: This is the Node Constructor. Value param is the value that the node will represent. Next (optional param) defaults to none and represents the next node in the list.
2. LinkedList init: This is the constructor for the actual linked list. Head (optional param) defaults to none and represents the head of the linked list.
3. LinkedList insert: Inserts a value to the head of the linked list. Takes in a value that the new node represents.
4. LinkedList includes: Searches the linked list for a specific value. Takes in value we are searching for and outputs a boolean to indicate whether or not the value was found.
5. LinkedList str: Produces a string representation of the linked list.