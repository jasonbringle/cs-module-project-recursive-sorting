# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0

    while i + j != elements:
        if i == len(arrA):
            merged_arr[i +j] = arrB[j]
            j += 1
        elif j == len(arrB):
            merged_arr[j + i] = arrA[i]
            i += 1
        elif arrA[i] > arrB[j]:
            merged_arr[i + j] = arrB[j]
            j += 1
        else: 
            merged_arr[i + j] = arrA[i]
            i += 1

    return merged_arr

# listOne = [1,2,4,5,6,7,8]
# listTwo = [5,66,77,88,99,345]
# print(merge(listOne, listTwo))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
