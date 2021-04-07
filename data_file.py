'''
Data file module to open and arrange the raw data.
'''

# Open the files that contain the texts (strings), assign strings to variables
text_1 = open( "/path/to/the/text/file/texts/textfile1.txt", encoding='utf-8' ).read()
text_2 = open( "/path/to/the/text/file/texts/textfile2.txt", encoding='utf-8' ).read()
text_3 = open( "/path/to/the/text/file/texts/textfile3.txt", encoding='utf-8' ).read()
#
#
#

# Arrange the variables into two tuples
text_list1 = (text_1, text_2, text_3)
text_list2 = (text_1, text_2, text_3)

# String labels used in distance matrices
names = ('text_1', 'text_2', 'text_3')


