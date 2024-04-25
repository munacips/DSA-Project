# Python3 code to linearly search x in arr[].
def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)








# Python3 code to implement iterative Binary
# Search.


# It returns location of x in given array arr
def binarySearch(arr, l, r, x):

    while l <= r:

        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")









# Python3 program to illustrate
# recursive approach to ternary search
import math as mt

# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):

    if (r >= l):

        # Find the mid1 and mid2
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3

        # Check if key is present at any mid
        if (ar[mid1] == key): 
            return mid1
        
        if (ar[mid2] == key): 
            return mid2
        
        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        if (key < ar[mid1]): 

            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar)
        
        elif (key > ar[mid2]): 

            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar)
        
        else: 

            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1, 
                                 mid2 - 1, key, ar)
        
    # Key not found
    return -1

# Driver code
l, r, p = 0, 9, 5

# Get the array
# Sort the array if not sorted
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5

# Key to be searched in the array
key = 5

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# Checking for 50

# Key to be searched in the array
key = 50

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# This code is contributed by 
# Mohit kumar 29




















# Python3 code to implement Jump Search
import math

def jumpSearch( arr , x , n ):
	
	# Finding block size to be jumped
	step = math.sqrt(n)
	
	# Finding the block where element is
	# present (if it is present)
	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
	
	# Doing a linear search for x in 
	# block beginning with prev.
	while arr[int(prev)] < x:
		prev += 1
		
		# If we reached next block or end 
		# of array, element is not present.
		if prev == min(step, n):
			return -1
	
	# If element is found
	if arr[int(prev)] == x:
		return prev
	
	return -1

# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number" , x, "is at index" ,"%.0f"%index)

# This code is contributed by "Sharad_Bhardwaj".














# Python3 program to implement
# interpolation search
# with recursion

# If x is present in arr[0..n-1], then
# returns index of it, else returns -1.


def interpolationSearch(arr, lo, hi, x):

	# Since array is sorted, an element present
	# in array must be in range defined by corner
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		# Probing the position with keeping
		# uniform distribution in mind.
		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
					(x - arr[lo]))

		# Condition of target found
		if arr[pos] == x:
			return pos

		# If x is larger, x is in right subarray
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1,
									hi, x)

		# If x is smaller, x is in left subarray
		if arr[pos] > x:
			return interpolationSearch(arr, lo,
									pos - 1, x)
	return -1

# Driver code


# Array of items in which
# search will be conducted
arr = [10, 12, 13, 16, 18, 19, 20,
	21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

# Element to be searched
x = 18
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
	print("Element found at index", index)
else:
	print("Element not found")

# This code is contributed by Hardik Jain



















# Python program to find an element x
# in a sorted array using Exponential Search

# A recursive binary search function returns 
# location of x in given array arr[l..r] is 
# present, otherwise -1
def binarySearch( arr, l, r, x):
	if r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element is present at 
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If the element is smaller than mid, 
		# then it can only be present in the 
		# left subarray
		if arr[mid] > x:
			return binarySearch(arr, l, 
								mid - 1, x)
		
		# Else he element can only be
		# present in the right
		return binarySearch(arr, mid + 1, r, x)
		
	# We reach here if the element is not present
	return -1

# Returns the position of first
# occurrence of x in array
def exponentialSearch(arr, n, x):
	# IF x is present at first 
	# location itself
	if arr[0] == x:
		return 0
		
	# Find range for binary search 
	# j by repeated doubling
	i = 1
	while i < n and arr[i] <= x:
		i = i * 2
	
	# Call binary search for the found range
	return binarySearch( arr, i // 2, 
						min(i, n-1), x)
	

# Driver Code
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)
if result == -1:
	print ("Element not found in the array")
else:
	print ("Element is present at index %d" %(result))

# This code is contributed by Harshit Agrawal
