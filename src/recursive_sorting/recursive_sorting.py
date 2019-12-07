# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    curr_index = 0
    counter1 = 0
    counter2 = 0
    while counter1 < len(arrA) or counter2 < len(arrB):
        if counter1 < len(arrA) and counter2 < len(arrB):
            if arrA[counter1] <= arrB[counter2]:
                merged_arr[curr_index] = arrA[counter1]
                counter1 += 1
            else:
                merged_arr[curr_index] = arrB[counter2]
                counter2 += 1
        elif counter2 < len(arrB):
            merged_arr[curr_index] = arrB[counter2]
            counter2 += 1
        else:
            merged_arr[curr_index] = arrA[counter1]
            counter1 += 1
        curr_index += 1
        print(f'current counters and index: {counter1}, {counter2}, {curr_index}')
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
