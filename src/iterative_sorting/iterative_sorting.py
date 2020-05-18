# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # First, we set two variables, one to track the current index, and one to track the smallest index of the unsorted values
        # This allows us to compare the value at the current index with the value at the smallest index
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        
        # Here, we write a for loop to go through the rest of the array, starting from the index of the last element to be sorted
        for j in range(cur_index + 1, len(arr)):
            # For each index, we compared the value at the j index with the value at the smallest index
            if arr[j] < arr[smallest_index]:
                # If the value at j is smaller than the value at the smallest index, we set the smallest index to be j
                smallest_index = j
        
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
