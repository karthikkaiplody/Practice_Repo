'''
Missing number in an array
    Given an array of size N-1 such that, 
    it can only contain distinct integers in the range of 1 to N.
    Find the missing element.

Example: 
Input:
N = 5
A[] = {1,2,3,5}
Output: 4

Input:
N = 10
A[] = {1,2,3,4,5,6,7,8,10}
Output: 9
'''
# Approach-1
''' 
We know that sum of N natural number is 1+2+3+...+n = n*(n+1)//2
So after finding the sum of n natural number as well as sum of given array.
The difference between both will give you the missing number in the array

Execution time approx: 0.30sec
Complexty: O(n)
'''
def missingNumber1(array, n):
    # Computing the total of n natural numbers
    total = n*(n+1)//2
    array_sum = 0    
    for i in array:
        array_sum +=i
    
    return (total-array_sum)


array = [1,2,3,5]
n = 5
print("Missing number is {}".format(missingNumber1(array, n)) )

