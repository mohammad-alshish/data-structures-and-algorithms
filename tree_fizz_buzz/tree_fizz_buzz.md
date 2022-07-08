# tree-fizz-buzz.



## Language: `Python`
## Challenge Type:  Code Challenge / Algorithm

## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tree_fizz_buzz/tree_fizz_buzz.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_tree_fizz_buzz.py)

## Challenge

Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree
- Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

1. If the value is divisible by 3, replace the value with “Fizz”
2. If the value is divisible by 5, replace the value with “Buzz”
3. If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
4. If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

 [WHITEBOARD](CC18.jpg)

## Approach & Efficiency

We tried to keep our code as simple as possible to the best performance by reducing space/Time complexity
so we end with the following

Big O:
1. Time complexity => O(N) 
2. Space complexity => O(N)

- we finish like this because The loop process --> the more the items in tree the more the time needed (Direct propotinoal)
- The Space also end like O(N) because The more the items in tree will make the new tree larger and take more space (Direct propotinoal)

## Solution

- declare a function called fizz_buzz.
- declare walk function.
- use if - else statments to check on our cases 
- use the recursive  to walk through tree
- return the new tree

The code the have test folder so you can run **pytest .\tests\test_Trees.py** and there is an example in the code file you can run it and check the output.