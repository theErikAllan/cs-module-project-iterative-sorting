def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # First, we set variables to the min and max indices
    # 0 is the first index
    # len(arr) - 1 is the final index
    low = 0
    high = len(arr) - 1

    # Then we write a while loop that runs as long as the lowest index is less than or equal to the highest, representing the narrowing of the possible indices which contain the target value
    while low <= high:
        # We initially grab the middle index value as a starting point, and convert it to an integer in case there are an even number of elements in the array
        middle = int((low + high) / 2)

        # Then we check to see if the target value could be in the left side of the array by checking if it's less than the element in the middle
        if target < arr[middle]:
            # If the value of the target element is less than the value at the middle index, we update the high index by removing the "right half" of the array
            high = middle - 1
        elif target > arr[middle]:
            # If the value of the target element is greater than the value at the middle index, we update the low index by removing the "left half" of the array
            low = middle + 1
        else:
            # Finally, if the value of the target element is not less than or greater than the value at the middle index, it must be equal, so we return the value of the final middle index
            return middle
    return -1  # not found
