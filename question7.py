#Authors: Group2

#function to count word redudancy in a text

def frequency_counter(text):
    """
    in the frequency_counter function, you enter a word and 
    it returns the occurrence of the word entered in a dictionary format
    """
    counter = {}
    for i in text:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] =1
    return counter


