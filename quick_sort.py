def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for i in range(len(array)):
            if pivot > array[0]: less.append(array[i])
            elif pivot == array[0]: equal.append(array[i])
            elif pivot < array[0]: greater.append(array[i])
            
        return quick_sort(less) + equal + quick_sort(greater)
    
    else:
        return array


print(quick_sort([4,2,3,5,1,2,3,6,3]))
