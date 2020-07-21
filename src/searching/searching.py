# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    '''
    The function must call itself
    The function must have a base case, 
    which is the simplest version of the problem 
    in which the answer is defined or known already
    The function must move towards the base case
    '''
    # base case
    if start <= end: 
        middle = (start + end) // 2
        guess = arr[middle]
        
        if guess == target:
            return middle

        # move toward base case
        elif guess > target: # exclude right half
            end = middle - 1 
            # recursive call
            return binary_search(arr, target, start, end)

        elif guess < target: # exclude left half
            start = middle + 1
            return binary_search(arr, target, start, end)
    else:
        return -1

        
    
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass




# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr = [-2, -1, 3, 5, 7]
target = 5
print("Binary:", binary_search(arr, target, start=0, end=len(arr)-1))