#Authors: Group2

import itertools #helper module

def number_display(number):
    """
    number_display takes in an integer n and outputs 
    a list with 1 once, 2 twice, 3 three times….n n-times
    """
    if number < 2:
        raise ValueError("ValueError exception thrown")
    else:
        result = [[i] * i for i in list(range(number))]
        result = list(itertools.chain.from_iterable(result))
        return result




