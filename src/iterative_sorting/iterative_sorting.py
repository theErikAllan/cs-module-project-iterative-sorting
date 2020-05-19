# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements, and we use n-1 because the value at the end of the array will become the maximum value so there's no need to sort it
    for i in range(0, len(arr) - 1):
        # First, we set two variables, one to track the current index as we move through the array, and one to track the index of the smallest value
        # This allows us to compare the value at the current index with the smallest value 
        cur_index = i
        index_of_smallest_value = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        
        # Here, we write a for loop to go through the rest of the array, starting from the index of the last element to be sorted
        for j in range(cur_index + 1, len(arr)):
            # In each loop, we compare the value at the j index with the smallest value
            if arr[j] < arr[index_of_smallest_value]:
                # If the value at j is smaller than the value at the smallest index, we set the index of the smallest value to be j, as j represents the index of the smallest value up to this point
                index_of_smallest_value = j
        
        # Finally, we swap the value at the current index with the smallest value we found during the loop
        arr[index_of_smallest_value], arr[cur_index] = arr[cur_index], arr[index_of_smallest_value]


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # First, we determine the length of the array for the for loop we will run 
    arr_len = len(arr)

    # Next, we set the for loop to run up to the last index, aka (arr_len - 1)
    for i in range(arr_len - 1):
        # Then we create a nested for loop that starts at the beginning of the array and goes through the remaining array elements: (arr_len - i -1) represents the length of the array minus the number of elements already sorted by the first for loop
        for j in range(0, arr_len - i - 1):
            # Next, for each element, we check to see if the value at the current index is greater than the value to the right of it
            if arr[j] > arr[j + 1]:
                # If the current value is greater than the one to the right, we swap the elements before resuming the for loop
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr


# STRETCH: implement the Count Sort function below
# Requires us to know the "max" value that we'll be sorting
# The maximum was arg so we could specify the max value
# The total range of data we'll be sorting sits between 0 and maximum
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return arr
    
    # if maximum is not given, we'll take the max value from the input array
    if maximum == -1:
        maximum = max(arr)

    # make a bunch of buckets
    buckets = [0 for i in range(maximum + 1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1
    
    # We have the counts of every value in our input array
    # Loop through our buckets, starting at the smallest index
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(count_sort(arr1))