def bubble_sort(array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i+1],array[i]
                sorted = False
    return array

print(bubble_sort([1,3,2,6,4,3]))
