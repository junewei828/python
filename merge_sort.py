# def merge(a, b):
#     """ Function to merge two arrays """
#     c = []
#     while len(a) != 0 and len(b) != 0:
#         if a[0] < b[0]:
#             c.append(a[0])
#             a.remove(a[0])
#         else:
#             c.append(b[0])
#             b.remove(b[0])
#     if len(a) == 0:
#         c += b
#     else:
#         c += a
#     return c

# # Code for merge sort


# def mergesort(x):
#     """ Function to sort an array using merge sort algorithm """
#     if len(x) == 0 or len(x) == 1:
#         return x
#     else:
#         middle = len(x)/2
#         a = mergesort(x[:middle])
#         b = mergesort(x[middle:])
#         return merge(a, b)


# alist = [54,26,93,17,77,31,44,55,20]
# print(mergesort(alist))

def mergeSort(alist):
    if len(alist) <= 1: return alist
    
    else:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
        
    return alist
            

alist = [54,26,93,17,77,31,44,55,20]
print(mergeSort(alist))

    
