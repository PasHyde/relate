

from relate import shingle

'''
Functions return a similarity value between a pair of strings (texts) using three different string similarity metrics:
Jaccard similarity coefficient, Sørensen_Dice, and Overlap coefficient.
'''
# Call tokenize function to shingle the strings
shingle = shingle.tokenize

def jaccard_similarity_coefficient(string_a, string_b):
    '''
    Function returns the Jaccard similarity coefficient between two strings. 

    Texts are divided (tokenized) into shingles of character length k (default shingle.length = 4) and treated as elements of a set.
    The tokenized strings are converted to sets and the Jaccard similarity coefficient calculated:
    (intersection / union == shingles shared between sets / number of shingles in both sets).

    Parameters:
    string_a : first string (text)
    string_b : second string (text)

    Returns:
    float: Jaccard coefficient * 100
    
    '''
    # Calculate intersection (& operator) == number of shingles shared between sets
    intersection = len(set(shingle(string_a)) & set(shingle(string_b)))
    # Calculate union (| operator) == number of shingles in both sets
    union = len(set(shingle(string_a)) | set(shingle(string_b)))
    # Return 6 digit float ranging between 0-100 (Jaccard similarity ranges between 0-1 by default)
    jaccard_similarity = ("%.6f" % ((intersection / union) * 100))
    return jaccard_similarity


def sørensen_dice(string_a, string_b):
    '''
    Function returns the Sørensen–Dice coefficient between two strings.

    Texts are divided (tokenized) into shingles of character length k (default shingle.length = 4) and treated as elements of a set.
    The tokenized strings are converted to sets and the Sørensen–Dice coefficient calculated:
    (intersection *2 / sum of the number of elements in each set ==
    shingles shared between sets x 2 / sum of the number of shingles in each set).

    Parameters:
    string_a : first string (text)
    string_b : second string (text)

    Returns:
    float: Sørensen–Dice coefficient * 100
    
    '''
    # Calculate intersection (& operator) = the number of shingles shared between sets
    intersection = len(set(shingle(string_a)) & set(shingle(string_b)))
    # Calculate the sum of the number of elements in each sets
    sum_of_elements = len(set(shingle(string_a))) + len(set(shingle(string_b)))
    # Return 6 digit float ranging between 0-100 (Sørensen-Dice coefficient ranges between 0-1 by default)
    sørensen_dice_coefficient = ("%.6f" % ((intersection *2 / sum_of_elements) * 100))
    return sørensen_dice_coefficient
        


def overlap_coefficient(string_a, string_b):
    '''
    Function returns the overlap coefficient between two strings.

    Texts are divided (tokenized) into shingles of character length k (default shingle.length = 4) and treated as elements of a set.
    The tokenized strings are converted to sets and the overlap coefficient calculated:
    (intersection / number of elements in the smaller set == shingles shared between sets /
    number of shingles in the smaller set).

    Parameters:
    string_a : first string (text)
    string_b : second string (text)

    Returns:
    float: overlap coefficient * 100
    '''
    # Calculate intersection (& operator) = the number of shingles shared between sets
    intersection = len(set(shingle(string_a)) & set(shingle(string_b)))
    # Return the smaller number of the two sets
    smaller_set = min(len(set(shingle(string_a))), len(set(shingle(string_b))))
    # Return 6 digit float ranging between 0-100 (overlap coefficient ranges between 0-1 by default)
    overlap_coefficient_similarity = ("%.6f" % ((intersection / smaller_set) * 100))
    return overlap_coefficient_similarity
    
# Use dictionary to call the functions
select= {
    'jaccard': jaccard_similarity_coefficient,
    'sørensen_dice': sørensen_dice,
    'overlap': overlap_coefficient
    }
