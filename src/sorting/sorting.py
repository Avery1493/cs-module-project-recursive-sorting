# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    indexA = 0
    indexB = 0


    # starting at the beginning of `a` and `b`
    # while len(A) >= 1 and len(B) >= 1:
        # 

    # compare the next value of each

    # add smallest to `merged_arr`


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    # base case
    if len(arr) > 1:
        middle = len(arr) // 2
        arrA = arr[0: middle]
        arrB = arr[middle::]
        # recursively call merge_sort() on LHS
        merge_sort(arrA)
        # recursively call merge_sort() on RHS
        merge_sort(arrB)
        # merge sorted pieces
        return merge(arrA, arrB)      
    else:
        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass



arr1 = [3, 2]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]
#print(merge_sort(arr4))
arrA = [3]
arrB = [2]
print(merge(arrA, arrB))