
# Assign  length of the shingles
length = 3

def shingle_letters(string):
    '''Function to divide a string (text) into shingles.

    The string is divided (tokenized) into smaller units called shingles of
    character length k (default length = 3). These partially overlaps
    to one another. The last characters (shingle length -1) are ignored.

    string = 'a fox jumps' --> shingle_letters(string) --> ['the ', 'he f', 'e fo', ' fox', 'fox ', 'ox j', 'x ju', ' jum', 'jump', 'umps']

    Parameters:
    string : a text

    Returns:
    list: shingles of character length k
    '''
  
    shingle = [string[i:i+length] for i in range(len(string)-(length-1))]
    return shingle

def shingle_words(string):
    '''Function to divide a string (text) into shingles.

    The string is divided (tokenized) into smaller units called shingles of
    word length k (default length = 3). These partially overlaps
    to one another. The last word (shingle length -1) are ignored.

    string = 'a brown fox jumps high' --> shingle_words(string) --> ['a brown fox', 'brown fox jumps', 'fox jumps high' ]

    Parameters:
    string : a text

    Returns:
    list: shingles of word length k
    '''
    
    # Split a string into words using white spaces
    shingle = string.split()
    shingles = [' '.join(shingle[i:i+length]) for i in range(len(shingle) - (length - 1))]
    return shingles

select= {
    'letters': shingle_letters,
    'words': shingle_words
    }
