def Selectionsort(arr) :
    for example_i in range(len(arr)-1):
        min_index = example_i
        for example_j in range(example_i +1,len(arr)):
            if arr[example_j] < arr[min_index]:
                min_index= example_j
        arr[example_i], arr[min_index] = arr[min_index], arr[example_i]

arr_i=[1,24,66,2,4,98,9]
Selectionsort(arr_i)
print(arr_i)
