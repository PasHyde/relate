
# Assign the length of the shingles
length = 4

def shingle(string):
    '''
    Function to divide a string (text) into shingles.

    The string is divided (tokenized) into smaller units called shingles of
    character length k (default length = 4). These partially overlaps
    to one another. The last characters (shingle length -1) are ignored.

    string = 'a fox jumps' --> shingle(string) == ['the ', 'he f', 'e fo', ' fox', 'fox ', 'ox j', 'x ju', ' jum', 'jump', 'umps']

    Parameters:
    string : a text

    Returns:
    list: shingles of character length k
    '''
    
    shingles = [string[i:i+length] for i in range(len(string)-(length-1))]
    return shingles
