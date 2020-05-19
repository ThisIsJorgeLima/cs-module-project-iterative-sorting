# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(i + 1, len(arr)):
            if arr[cur_index] > arr[n]:
                cur_index = n

            # TO-DO: swap
            # Your code here
            arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for a in range(len(arr) - 1):
        for b in range(0, len(arr)-a-1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1], = arr[b+1], arr[b]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
