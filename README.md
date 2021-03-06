# relate

Relate is an open-source python package to estimate similarities between strings (texts) using character- or token-based string similarity metrics. It takes a plain text file as input and returns a symmetric matrix of pairwise distances between the strings. This can be used for hierarchical clustering, phylogenetic or network analysis to investigate the relationships between different versions of a text.

The modules included in relate can be used together or separately.

The shingle module divides or tokenizes the texts into shingles of character or word length k, specified by a user. For more information about the shingling method, see [here](https://en.wikipedia.org/wiki/W-shingling).

```python
from relate import shingle
# Select the shingle length 
shingle.length = 2
# Select the shingle type: 'letters' or 'words'
shingle = shingle.select['letters']
text = 'the fox jumps' 
print(shingle(text))
['th', 'he', 'e ', ' f', 'fo', 'ox', 'x ', ' j', 'ju', 'um', 'mp', 'ps']
```
or 
```python
shingle = shingle.select['words']
print(shingle(text))
['the fox', 'fox jumps']
```

The similarity between pairs of strings is estimated by using character-based string metrics Levenshtein and Hamming similarity or token-based string metrics Jaccard similarity coefficient, Sorensen-Dice, and Overlap coefficient. Character-based metrics estimate the similarities directly from strings without using the shingling module. When applying the token-based methods, the shingling module is used, converting each string into a set and the shingles to elements of that set. For more information about the used string metrics, see [here](https://en.wikipedia.org/wiki/String_metric).

```python
# An example of using the character-based metrics
from relate import metrics
text1 = 'the fox jumps'
text2 = 'the fox waits'
# Select preferable character-based metrics from two options: 'levenshtein', 'hamming'
measure = metrics.select['levenshtein']
print(measure(text1, text2))
69.23076923076923
```
or 
```python
# An example of using the token-based metrics
from relate import shingle, metrics
# Select the shingle length 
shingle.length = 2
# Select the shingle type: 'letters' or 'words'
metrics.shingle = shingle.select['letters']
# Select preferable token-based metrics from three options: 'jaccard', 'overlap', 'sorensen_dice'
measure = metrics.select['sorensen_dice']
print(measure(text1, text2))
58.333333
```
The matrixes module automatically arranges the estimated values into a symmetric matrix. All punctuation marks and capitals should be removed from the texts and the pronunciation standardized. The data should be arranged as following:

```python
text1 = 'the fox jumps'
text2 = 'the fox waits'
text3 = 'one fox jumps'
text4 = 'second fox waits'
# Arrange all texts into two tuples:
texts1 = (text1,text2,text3,text4)
texts2 = (text1,text2,text3,text4)
# Names or IDs of the analyzed texts
matrixes.names = ('text1','text2','text3','text4')
```
The module returns a similarity matrix (values taken directly from the string metrics), a distance matrix (1-string metric) with or without standardizing function:
![image](https://user-images.githubusercontent.com/79587588/114005450-38afd400-9868-11eb-97ff-dca35310751a.png) 
estimated value - mean / standard deviation
```python
from relate import shingle, metrics, matrixes
# Select the shingle length
shingle.length = 2
# Select the shingle type
metrics.shingle = shingle.select['letters']
# Select used similarity metrics
measure = metrics.select['sorensen_dice']
# Select the type of values used in the matrix: 'similarity', 'distance', 'st_similarity', 'st_distance'.
matrix = matrixes.select['distance']
result = matrix(measure,texts1, texts2)
print(result)
            text_1     text_2     text_3     text_4
text_1   0.000000  41.666667  16.666667  70.370370
text_2  41.666667   0.000000  58.333333  33.333333
text_3  16.666667  58.333333   0.000000  62.962963
text_4  70.370370  33.333333  62.962963   0.000000
```
Symmetric matrix organizes and visualizes the data in a clear manner. However, one may wish to manipulate the output. For instance, some require the upper half of the matrix only:

```python
import numpy as np
print(np.triu(result))
[[ 0.       41.666667 16.666667 70.37037 ]
 [ 0.        0.       58.333333 33.333333]
 [ 0.        0.        0.       62.962963]
 [ 0.        0.        0.        0.      ]]
```
Or print the data as condensed matrix using scipy:

```python
import scipy.spatial.distance as ssd
result = ssd.squareform(result)
print(result)
[41.666667 16.666667 70.37037  58.333333 33.333333 62.962963]
```

This, on the other hand, can be used as input in scipy hierarchical clustering algorithms: 

```python
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(result, method='ward'), labels = names, leaf_font_size= 10, orientation = 'top',
                      color_threshold = 2, leaf_rotation=45)
plt.show()
```
![image](https://user-images.githubusercontent.com/79587588/114025796-3193c080-987e-11eb-84c5-fb224ca04662.png)

