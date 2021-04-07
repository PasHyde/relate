
import math
from relate import metrics, data_file
import pandas as pd


'''
Functions return different symmetric matrices (similarity and distance) using different calculations:
string similarity metrics with (or without) standardizing function.
'''
# Call string similarity metrics (jaccard,sørensen_dice or overlap) from metrics module 
metrics = metrics.metrics
names = data_file.names

def similarity_matrix(metrics, text_list1, text_list2):
    '''
    Function returns a symmetric similarity matrix, which has the same number of rows and
    columns (n x n).
    
    Parameters:
    metrics: 'jaccard' (jaccard_similarity_coefficient),
             'sørensen_dice' (sørensen_dice coefficient),
             'overlap' (overlap_coefficient)
    text_list1: first tuple (tokenized strings stored in the items of the tuple)
    text_list2: second tuple (tokenized strings stored in the items of the tuple)

    Returns:
    matrix: n x n symmetric similarity matrix
    '''
   
    # Compare a pair of tokenized strings at a time stored in tuples text_list1 and text_list2, return list and 
    # sublists corresponding the number of strings in the dataset
    SM = [[(metrics (a,b)) for a in text_list1] for b in text_list2]
    # Convert sublists into a matrix using pandas Dataframe
    matrix = pd.DataFrame(SM, columns=names, index=names)
    # show the whole matrix
    pd.set_option('display.width', None)
    return matrix

def distance_matrix(metrics, text_list1, text_list2):
    '''
    Function returns a symmetric distance matrix, which has the same number of rows and
    columns (n x n).

    Parameters:
    metrics: 'jaccard' (jaccard_similarity_coefficient),
             'sørensen_dice' (sørensen_dice coefficient),
             'overlap' (overlap_coefficient)
    text_list1: first tuple (tokenized strings stored in the items of the tuple)
    text_list2: second tuple (tokenized strings stored in the items of the tuple)

    Returns:
    matrix: n x n symmetric distance matrix
    '''
    # Compare a pair of tokenized strings at a time stored in tuples text_list1 and text_list2, return list of
    # distance values ((1-metrics)*100) and sublists corresponding the number of strings in the dataset
    DM = [[100-float(metrics (a,b)) for a in text_list1] for b in text_list2]
    # Convert sublists into a matrix using pandas Dataframe
    matrix = pd.DataFrame(DM, columns=names, index=names)
    # show the whole matrix
    pd.set_option('display.width', None)
    return matrix

def standardized_similarity_matrix(metrics, text_list1, text_list2):
    '''
    Function returns a symmetric similarity matrix, which has the same number of rows
    and columns (n x n) with standardized values. The used standardizing function:
    original value - mean of the values in the dataset / standard deviation of the values in the dataset.

    Parameters:
    metrics: 'jaccard' (jaccard_similarity_coefficient),
             'sørensen_dice' (sørensen_dice coefficient),
             'overlap' (overlap_coefficient)
    text_list1: first tuple (tokenized strings stored in the items of the tuple)
    text_list2: second tuple (tokenized strings stored in the items of the tuple)

    Returns:
    matrix: n x n symmetric similarity matrix with standardized values
    '''
    # Compare a pair of tokenized strings at a time stored in tuples text_list1 and text_list2, return list of similarity values
    SM1 = [float(metrics (a,b)) for a in text_list1 for b in text_list2]
    # Ignore instances where the strings are compared to itself, resulting to value 100 (= 100 % similarity)
    SM  = [x for x in SM1 if x != 100]
    # Calculate mean of all the values (skipping value 100) in the dataset
    mean = sum(SM)/(len(SM))
    # The first step to calculate the standard deviation is to subtract the mean
    subtract = [x - mean for x in SM]
    # Square the mean from the previous step
    square = [x ** 2 for x in subtract]
    # Work out the mean of the squared values (the number of values -1, because one is usually dealing with a sample, not the whole population)
    divide = sum(square)/(len(SM)-1)
    # Take square root of the result == standard deviation
    square_root = math.sqrt(divide)
    standard_deviation = square_root
    # Apply the standardization function to all values in the dataset, skip when the string is compared to itself
    standardize = [0 if x == 100.0 else (x- mean)/standard_deviation for x in SM1]
    # Return a list containing sublists corresponding the number of strings in the dataset
    standardize = [standardize[x:x+len(text_list1)] for x in range(0, len(standardize), len(text_list1))]
    # Convert sublists into a matrix using pandas Dataframe
    matrix = pd.DataFrame(standardize, columns=names, index=names)
    # show the whole matrix
    pd.set_option('display.width', None)
    return matrix

def standardized_distance_matrix(metrics, text_list1, text_list2):
    '''
    Function returns a symmetric distance matrix, which has the same number of rows
    and columns (n x n) with standardized values. The used standardizing function:
    original value - mean of the values in the dataset / standard deviation of the values in the dataset.

    Parameters:
    metrics: 'jaccard' (jaccard_similarity_coefficient),
             'sørensen_dice' (sørensen_dice coefficient),
             'overlap' (overlap_coefficient)
    text_list1: first tuple (tokenized strings stored in the items of the tuple)
    text_list2: second tuple (tokenized strings stored in the items of the tuple)

    Returns:
    matrix: n x n symmetric distance matrix with standardized values
    '''
    # Compare a pair of tokenized strings at a time stored in tuples text_list1 and text_list2, return list of distance values ((1-metrics)*100)
    DM1 = [100-float(metrics (a,b)) for a in text_list1 for b in text_list2]
    # Ignore instances where the strings are compared to itself, resulting to value 0 (= 0 % distance)
    DM  = [x for x in DM1 if x != 0]
    # Calculate mean of all the values (skipping instances of 0) in the dataset
    mean = sum(DM)/(len(DM))
    # The first step to calculate the standard deviation is to subtract the mean
    subtract = [x - mean for x in DM]
    # Square the mean from the previous step
    square = [x ** 2 for x in subtract]
    # Work out the mean of the squared values (the number of values -1, because one is usually dealing with a sample, not the whole population)
    divide = sum(square)/(len(DM)-1)
    # Take square root of the result == standard deviation
    square_root = math.sqrt(divide)
    standard_deviation = square_root
    # Apply the standardization function to all values in the dataset, skip when the string is compared to itself
    standardize = [0 if x == 0.0 else (x- mean)/standard_deviation for x in DM1]
    # Return a list containing sublists corresponding the number of strings in the dataset
    standardize = [standardize[x:x+len(text_list1)] for x in range(0, len(standardize), len(text_list1))]
    # Convert sublists into a matrix using pandas Dataframe
    matrix = pd.DataFrame(standardize, columns=names, index=names)
    # show the whole matrix
    pd.set_option('display.width', None)
    return matrix

# Use dictionary to call the functions
matrix={
    'similarity': similarity_matrix,
    'distance': distance_matrix,
    'st_similarity': standardized_similarity_matrix,
    'st_distance': standardized_distance_matrix
    }

