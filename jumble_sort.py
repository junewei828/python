import string

def jumble_sort(array):
    alpha = list(string.ascii_lowercase)

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array)-1):
            if alpha.index(array[i]) > alpha.index(array[i + 1]):
                array[i],array[i + 1] = array[i + 1], array[i]
                sorted = False

    return array



print(jumble_sort(['b','a','g','s','d']))


