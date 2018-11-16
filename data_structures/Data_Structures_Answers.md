Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    O(n) since we traverse each element once.

2. What is the space complexity of your `depth_first_for_each` function?
    O(n) since we would at worst case need to hold all the nodes in the stack.

3. What is the runtime complexity of your `breadth_first_for_each` method?
    O(n) since we are traversing each node once.

4. What is the space complexity of your `breadth_first_for_each` method?
    In the worst case, we would need to hold all nodes in the queue, so space complexity is O(n).


5. What is the runtime complexity of your `heapsort` function?

Heapsort's runtime complexity is O(n log(n)) quasilinear time in the worst case.

It is this way because each iteration of n has the potential for two pivots, and each pivot also has the potential for two more pivots. Each time n doubles, we'll need to perform one additional operation (i.e. determining the pivot point). Therefore, in the worst case, we'll perform the operation O(n log(n)) number of times.

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

Since we are returning a new array of data, the space complexity is O(n), as we must account for a point in memory for each new data point in the new array.

If we were to modify the array in place, our space complexity would be O(1), as the memory allocation would be constant throughout the sorting operation.