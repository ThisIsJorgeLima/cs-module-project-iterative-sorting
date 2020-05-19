# This array is already sorted:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# assume array 'arr' is sorted


def binary_search(arr, target):
    # let's figure out the total size of the arr
    # returns the index of the target if it exists in the arr
    # if it's not in the arr, othersie, retirns - 1
    left = 0
    right = len(arr) - 1

    while left <= right:  # our loop
        # find the midpoint
        mid = (left + right) // 2  # // = divided

        # lets check to see if the midpoint element is our target
        if arr[mid] == target:
            return mid

        # check to see if the element should be on the left or right side of our midpoint
        if arr[mid] < target:
            # so were going to toss out the left side of the arr
            left = mid + 1
            # otherwise, arr[mid] > bigger than our target
        else:
            # toss out the right side of the arr because the lement has to be on the left side
            right = mid - 1


# we didn't find the element
    return - 1
