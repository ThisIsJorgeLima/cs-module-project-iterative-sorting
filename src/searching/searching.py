def linear_search(arr, target):
    for n in range(len(arr)):
        if arr[n] == target:
            return n

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # returns the index of the target if it exists in the arr
    # if it's not in the arr, othersie, retirns - 1
    left = 0
    right = len(arr) - 1
    print("left", left, "\nright", right)

    while left <= right:  # our loop
        # find the midpoint
        mid = (left + right) // 2  # // = divided
        print("\nmid", mid)

        # lets check to see if the midpoint element is our target
        if arr[mid] == target:
            return mid

        # check to see if the element should be on the left or right side of our midpoint
        if arr[mid] < target:
            # so were going to toss out the left side of the arr
            left = mid + 1
            print("left", left)
            # otherwise, arr[mid] > bigger than our target
        else:
            # toss out the right side of the arr because the lement has to be on the left side
            right = mid - 1
            print("right", right)

    # we didn't find the element
    return - 1
