#Authors: Group2

# function to replace whitespaces  with single spaces


def whitesp_remove(text):
    """ 
    whitesp_remove takes in a text, first replace whitespace into single
    lines, then removes trailing spacs with strip method.

    """
    text = text.replace("  ", "")
    
    return text.strip()


