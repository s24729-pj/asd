def is_empty(array):
    if len(array) == 0:
        return True
    else:
        return False


def glowa(array):
    return array[0]


def ogon(array):
    tmp_array = array
    tmp_array.pop(0)
    return tmp_array


def jedna_tablica(arr1, arr2):
    if not is_empty(arr1) and not is_empty(arr2):
        if glowa(arr1) <= glowa(arr2):
            print(glowa(arr1))
            jedna_tablica(arr2, ogon(arr1))
        else:
            print(glowa(arr2))
            jedna_tablica(ogon(arr2), arr1)


array1 = [1, 3, 4, 7, 8]
array2 = [2, 5, 6, 9, 12]

jedna_tablica(array1, array2)
