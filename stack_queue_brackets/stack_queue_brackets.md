# Data Structures and Algorithms

## Language: `Python`
## Challenge Type: ` Code Challenge / Algorithm`


# stack-queue-brackets

## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/stack_queue_brackets/stack_queue_brackets.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_stack_queue_brackets.py)

## Challenge13

Create a function that takes in a string and returns true or false depending on whether or not the brackets ('{}', '[]', '()') are balanced.


## Whiteboard Process
[WhiteBoard](CC13.jpg)

## Approach & Efficiency
Using a stack, I iterate through the string. 
The opening brackets are pushed onto the stack and then when a closing bracket is found, 
the corresponding opening bracket is popped out from the stack for comparing
If the stacks ends up being empty at the end, return true.

- I try to keep it simple by using one for loop so we end with complexity as the following:
1. Space: O(N)
2. Time: O(N)