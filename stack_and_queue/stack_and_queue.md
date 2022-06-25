# Data Structures and Algorithms

## Language: `Python`
## Challenge Type: `New Implementation`


# stack-and-queue
## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/stack_and_queue/stack_and_queue.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_stack_and_queue.py)

## Challenge10

Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.

## Whiteboard Process
No Whiteboard for this code challenge.

## Approach & Efficiency
1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception

## API
### Stack:
1. method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
2. method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
3. Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
4. method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
### Queue:
1. Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
2. Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
3. Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
4. Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
