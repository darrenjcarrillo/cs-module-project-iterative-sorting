def linear_search(arr, target):
    # Your code here
    n = -1  # set counter

    # loop every element in the array
    for i in arr:
        # increment the counter
        n += 1
        # if the element is the same as the target, return index
        if i == target:
            return n

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # set low
    low = 0
    # set high to the length of the array minus 1
    high = len(arr) - 1

    # loop over the array, while low is less than or equal to high
    while low <= high:
        # calculate the index by adding high and low and floor divide by 2
        mid = (low + high) // 2
        # set select midpoint element in the array
        mid_point = arr[mid]
        # Case 1 - the mid_point is correct
        if mid_point == target:
            # if true, return element
            return mid
        # Case 2 - if element we are searching is Less than the element in the middle
        elif mid_point <= target:
            # if true, change low value to mid + 1
            low = mid+1
        else:
            # else if mid_point is greater than or equal to high
            # change high value to mid - 1
            high = mid-1

    return -1  # not found
