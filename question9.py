#Authors: Group2

def array_dif(arrA, arrB):
    """
    array_dif takes in two arrays where length(arrB) > length(arrA)
    and returns the elements of arrB which are not in arrA
    """
    if len(arrA)> len(arrB): 
        raise TypeError("TypeError exception thrown")
    else:
        missing_elt = set(arrB) - set(arrA)
        return missing_elt

# print(array_dif([8,1,3,5,9,78],[8,1,2,3]))



