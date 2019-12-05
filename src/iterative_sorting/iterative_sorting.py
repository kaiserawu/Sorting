# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        curr_item = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = curr_item

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    complete = False

    while not complete:
        complete = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                complete = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if any(elem < 0 for elem in arr):
        return "Error, negative numbers not allowed in Count Sort"
    if len(arr) == 0:
        return arr
    
    max_count = max(arr) + 1
    count = [0] * max_count

    for i in range(len(arr)):
        count[arr[i]] += 1

    total_count = count[0]
    for j in range(1, max_count):
        total_count += count[j]
        count[j] = total_count

    result = [None] * len(arr)
    for item in arr:
        result[count[item] - 1] = item
        count[item] -= 1

    arr = result
    return arr