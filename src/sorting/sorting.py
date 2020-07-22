# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    indexA = 0
    indexB = 0

    # starting at the beginning of `a` and `b`
    while indexA < len(arrA) and indexB < len(arrB):
        # compare the next value of each
        if arrA[indexA] < arrB[indexB]:
            # add smallest to `merged_arr`
            merged_arr.append(arrA[indexA])
            indexA += 1
        else:
            merged_arr.append(arrB[indexB])
            indexB += 1
            
    merged_arr += arrA[indexA:]
    merged_arr += arrB[indexB:]

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    # base case
    if len(arr) > 1:
        middle = len(arr) // 2

        # recursively call merge_sort() on LHS
        arrA = merge_sort(arr[0: middle])
        # recursively call merge_sort() on RHS
        arrB = merge_sort(arr[middle::])

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
arrA = [1,3]
arrB = [2,6]
print(merge(arrA, arrB))