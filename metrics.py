

from relate import shingle
import sys
from polyleven import levenshtein

'''
Functions return a similarity value between a pair of strings (texts) using four different string similarity metrics:
Jaccard similarity coefficient, Sorensen_Dice, Overlap coefficient and Hamming.
'''
# Call shingle functions to tokenize the strings
shingle = shingle.select['letters']


def jaccard_similarity_coefficient(string_a, string_b):
    '''
    Function returns the Jaccard similarity coefficient between two strings.

    Texts are divided (tokenized) into shingles of character length k (default shingle.length = 3) and treated as elements of a set.
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


def sorensen_dice(string_a, string_b):
    '''
    Function returns the Sorensen–Dice coefficient between two strings.

    Texts are divided (tokenized) into shingles of character length k (default shingle.length = 3) and treated as elements of a set.
    The tokenized strings are converted to sets and the Sorensen–Dice coefficient calculated:
    (intersection *2 / sum of the number of elements in each set ==
    shingles shared between sets x 2 / sum of the number of shingles in each set).

    Parameters:
    string_a : first string (text)
    string_b : second string (text)

    Returns:
    float: Sorensen–Dice coefficient * 100
    
    '''
    # Calculate intersection (& operator) = the number of shingles shared between sets
    intersection = len(set(shingle(string_a)) & set(shingle(string_b)))
    # Calculate the sum of the number of elements in each sets
    sum_of_elements = len(set(shingle(string_a))) + len(set(shingle(string_b)))
    # Return 6 digit float ranging between 0-100 (Sorensen-Dice coefficient ranges between 0-1 by default)
    sorensen_dice_coefficient = ("%.6f" % ((intersection *2 / sum_of_elements) * 100))
    return sorensen_dice_coefficient
        


def overlap_coefficient(string_a, string_b):
    '''
    Function returns the overlap coefficient between two strings.

    Texts are divided (tokenized) into shingles of character length k (default shingle.length = 3) and treated as elements of a set.
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
    

def hamming_similarity(string_a, string_b):
    '''
    Function returns the Hamming similarity between two strings.
    
    Hamming similarity between two equal-length strings is the number of positions at which the corresponding characters are the same. For example:
    string_a = 'manuscript'
    string_b = 'autoscript'
    hamming_similarity = 6
    
    Parameters:
    string_a : first string (text)
    string_b : second string (text)

    Returns:
    float: hamming_similarity / number of characters in either strings * 100 = hamming_similarity in %.
    '''
    # Check whether the strings are of egual length
    [a if len(string_a) == len(string_b) else sys.exit("error: strings must be of equal length") for a in (string_a, string_b)]
    # Pair each character together from the two strings
    zipped = list(zip(string_a, string_b))
    # Ignore quoestion marks and the character that are paired with it (a user can insert here whatever characters or symbols one wishes to ignore from the strings)
    ignore = '?'
    [[zipped.remove(subl) for m in ignore if m in subl]for subl in zipped[:]]
    # Sum up all the characters that are the same in both strings (agreements)
    agreements = sum(x == y for x, y in zipped)
    # Calculate the hamming distance (agreements divided by the length of the string). Returns 6 digit float.
    hamming = ("%.6f" % (agreements / len(zipped) *100))
    return hamming

def levenshtein_similarity(string_a, string_b):
    '''
    Function returns the Levenshtein similarity between two strings.

    Levenshtein distance is defined as the smallest number of edit operations (insertion, deletion, and substitution)
    required to transform one string into another.
    string_a = 'the fast brown fox'
    string_b = 'the slow brown fox'
    Levenshtein distance = 4

    This is converted into a similarity value by using the following formula:
    1-levenshtein distance/max(string1, string2)
    levenshtein_similarity = 1- 4/18 = 0.778

    Parameters:
    string_a : first string (text)
    string_b : second string (text)

    Returns:
    float: levenshtein_similarity * 100
    '''
    # Calculate the Levenshtein distance using polyleven (Myers algorithm)
    levenshtein_distance = levenshtein(string_a, string_b)
    # Calculate the Levenshtein similarity
    levenshtein_sim = (1-levenshtein_distance/max(len(string_a), len(string_b)))*100
    return levenshtein_sim
    
    
# Use dictionary to call the functions
select= {
    'jaccard': jaccard_similarity_coefficient,
    'sorensen_dice': sorensen_dice,
    'overlap': overlap_coefficient,
    'hamming': hamming_similarity,
    'levenshtein': levenshtein_similarity
    }
