Add your answers to the Algorithms exercises here.

**Exercise I**

a) The time complexity of this operation is O(n) linear time. The break condition of the loop is n^3 while the arithmetic addition sums n^2. Thus, we would need to sum n^2 * n number of times to reach n^3. Consider: n^3 = n^2 * n


b) The time complexity of this operation is n^c quadratic time. Each nested loop depends on the value of "i" in the first loop, which is time complexity O(n) linear time. Therefore, we are deadling with n linear time, 4 different times, which gives us O(n^4).

c) The time complexity of this operation is O(n) linear time, because we're recursively calling n-1 until n reaches 0. Therefore, we call the function n times. Consider: n - n = 0

**Exercise II**

The fastest way to solve the egg drop problem in this instance would be a binary search, or using the half-interval approach. Since we know the value of n, and can assume n remains a constant throughout the search, we simply start by dropping the egg from the middle floor of the building. 

If it breaks, we move the upper range to the middle floor, and drop from the middle of the new range. 

If it doesn't break, we move the lower range to the middle floor, and drop from the middle of this new range.

We can keep tightening the range of the floors until we're left with two data points. 
The distance between them is:
upper: n
lower: n - 1

From here, we can determine that the upper value is the unsafe range, and the lower value is our safe range.
