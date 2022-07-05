# Breadth-first Traversal.



## Language: `Python`
## Challenge Type:  Code Challenge / Algorithm

## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/Trees/Trees.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_Trees.py)

## Challenge

Write a function called breadth first that  have
- Arguments <-- tree
- Return --> list of all values in the tree, in the order they were encountered


## Whiteboard Process

 [WHITEBOARD](CC17.jpg)

## Approach & Efficiency

We tried to keep our code as simple as possible to the best performance by reducing space/Time complexity
so we end with the following

Big O:
1. Time complexity => O(N) 
2. Space complexity => O(N)

- we finish like this because  While loop process --> the more the items in tree the more the time needed (Direct propotinoal)
- The Space also end like O(N) because The more the items in tree will make the array larger and take more space (Direct propotinoal)

## Solution
- declare a method breadth_first
- Import queue class to use it methods.
- declare empty array.
- use while to go through left and right when change the root add the root value to the list
- return the list

The code the have test folder so you can run **pytest .\tests\test_Trees.py** and there is an example in the code file you can run it and check the output.