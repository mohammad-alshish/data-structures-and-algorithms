# Hash Tables

## Language: `Python`
## Challenge Type: ` Code Challenge / New Implementation`


## Challenge Hash Table

## [Code](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/hash_tables/hash_tables.py)
## [tests](https://github.com/mohammad-alshish/data-structures-and-algorithms/blob/main/tests/test_hash_tables.py)


## Challenge

Implement a Hashtable Class with the following methods:
- set 
- get
- contains
- keys
- hash

The code should do the next functionality:

1. Setting a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully returns a list of all unique keys that exist in the hashtable
5. Successfully handle a collision within the hashtable
6. Successfully retrieve a value from a bucket within the hashtable that has a collision
7. Successfully hash a key to an in-range value

## Whiteboard Process
NO WHITEBOARD FOR THIS CODE CHALLENGE.

## Approach & Efficiency
- All of the methods above exist in the Hashtable class.
- The hash table is instantiated with 1024 buckets that have a default value of None.
- Collisions are handled with the linked list data structure.

### Big O:
the following table will show Big(O) for each method

| **Method** | **Time** | **Space** |
|------------|----------|-----------|
| hash       | O(1)     | O(1)      |
| add        | O(1)     | O(1)      |
| get        | O(n)     | O(n)      |
| contain    | O(n)     | O(n)      |
| key        | O(n)     | O(n)      |



## API 
> The code have test folder so you can run **`>>pytest .\tests\test_hash_tables.py`** and there is an example in the code file you can run it and check the output.

the Following table is like small descrition for each method 

| **Method** | **Params** | **Output**      |
|------------|------------|-----------------|
| hash       | key        | hash code (int) |
| add        | key        | None            |
| get        | key,val    | value           |
| contain    | key        | True or False   |
| key        | none       | array           |