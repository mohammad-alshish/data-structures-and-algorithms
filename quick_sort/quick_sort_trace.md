# Quick Sort
- Quick sort is a divide and conquer algorithm. 
- This algorithm utilizes pivots and partitions to sort the input array.
- since this algorithm lay on three functions we will trace each one to make everything clear. 

## Pseudo Code
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)![](../../Desktop/My Files/CCC22.jpg)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
## Trace 
- ***Sample array: [8,4,23,42,16,15].***  
- - ***Output array: [4,8,15,16,23,42].*** 
   
### quick_sort function tracing:
1. Our function takes in an array, the first index position (0), and the last index position (len(arr)-1). 
2. We pass the array and the index positions to our partition method and cache it in a variable position. 
3. We then call quick_sort recursively:
```
> quick_sort(arr, left, position - 1) ----->
> quick_sort([8,4,23,42,16,15], 0, position - 1)
```
4. We then call quick_sort recursively again with different arguments:
```
> quick_sort(arr, position + 1, right) ------->
> quick_sort([8,4,23,42,16,15], position + 1, 5)
```
5. Once the above recursion calls are finished, the new sorted array is returned. 

### Partition function tracing:
1. We pass the partition function the full input array, the first index, and the second index:
```
> position = partition(arr, left, right) ----->
> position = partition([8,4,23,42,16,15], 0, 5)
```
2. Define pivot variable as the last item in input array.
3. Define low which will be 0 - 1. 
4. Initiate a for loop in range from left to right. In our case, it will be from -1 to 5.
5. In our for loop, i represents the index. Check if the value in the array at each index is less than or equal to pivot (last value in array).
6. If the above is true, increment low by 1 and call our third method, swap, with the array, value of i, and value of low (after it was incremented). 
7. If the if statement was false, then we move on to the next iteration to see if the condition is true of false.
8. Once we break from the for loop, we call swap with the array, right value, and low value plus 1. 
9. Finally, 

### Swap function tracing:
1. Swap will take in an array, i, and low. 
2. First, we assign variable temp to the value at arr[i]. 
3. Then, we assign arr[i] to equal arr[low].
4. Finally, we set arr[low] to equal temp. 
                 
### Efficieny:
1. Time: O(n^2): Time will be proportional to the number of digits in n.
2. Space: O(n): logarithmic complexity - happens with functions that deal with recursion. Space increases by k/2.  