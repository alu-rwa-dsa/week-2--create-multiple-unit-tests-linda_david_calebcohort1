#Authors: Group2


from itertools import chain #helper module

def list_combinator(array):
    """
    list_combinator takes an array of arrays, merge the arrays inside and
    returns one array containing elements that were in the array of arrays(with no duplicate)
    """

    new_array =  set((chain.from_iterable(array)))
    return new_array
    

