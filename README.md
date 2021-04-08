# relate

Relate is an open-source python package to estimate the similarities between strings (texts) using k-shingling and string metrics. It takes a plain text file as input and returns a symmetric matrix that can be used for hierarchical clustering or phylogenetic analysis to investigate the relationships between different versions of a text.

The modules included in relate can be used together or separately.

The shingle module divides or tokenizes the texts into shingles of character length k, specified by a user:

```python
from relate import shingle
shingle.length = 2
shingle = shingle.tokenize
text = 'a fox jumps' 
print(shingle(text))
['th', 'he', 'e ', ' f', 'fo', 'ox', 'x ', ' j', 'ju', 'um', 'mp', 'ps']
```

The metrics module treats each text as a set and the shingles as elements of a set. The similarity between the pairs of texts is estimated by using string metrics: Jaccard similarity coefficient, Sørensen_Dice, or Overlap coefficient. For more information about the used string metrics, see [here](https://effectivesoftwaredesign.com/2019/02/27/data-science-set-similarity-metrics/).

```python
from relate import shingle, metrics
shingle.length = 2
text_1 = 'the fox jumps'
text_2 = 'the fox waits'
# User selects the preferable metrics from three options: 'jaccard', 'sørensen_dice', 'overlap'
similarity = metrics.select['sørensen_dice']
print(similarity(text_1, text_2))
58.333333
```

The matrix module automatically arranges the estimated values as a symmetric matrix. The plain text files can be opened and arranged using the data_file module. All punctuation marks and capitals should be removed from the texts and the pronunciation standardized. The data should be arranged into the data_file module as following: 

```python
text_1 = 'the fox jumps'
text_2 = 'the fox waits'
text_3 = 'one fox jumps'
text_4 = 'second fox waits'
# Arrange all texts into two tuples:
all_texts1 = (text_1,text_2,text_3,text_4)
all_texts2 = (text_1,text_2,text_3,text_4)
# Names or IDs of the analyzed texts
names = ('text_1','text_2','text_3','text_4')
```

The module returns a similarity matrix (values taken directly from the string metrics), a distance matrix (1-string metric) with or without standardizing function:
![image](https://user-images.githubusercontent.com/79587588/114005450-38afd400-9868-11eb-97ff-dca35310751a.png) 
estimated value - mean / standard deviation

```python
from relate import shingle, metrics, matrix, data_file
texts1 = data_file.all_texts1
texts2 = data_file.all_texts2
shingle.length = 2
similarity = metrics.select['sørensen_dice']
# Without standardizing function: 'similarity','distance'. With the function: 'st_similarity', 'st_distance' 
matrix = matrix.select['distance']
result = matrix(similarity,texts1, texts2)
print(result)
            text_1     text_2     text_3     text_4
text_1   0.000000  41.666667  16.666667  70.370370
text_2  41.666667   0.000000  58.333333  33.333333
text_3  16.666667  58.333333   0.000000  62.962963
text_4  70.370370  33.333333  62.962963   0.000000

```
This is a clear way to organize and visualize the data. However, one may wish to manipulate the output. For instance, some require the upper half of the matrix only:

```python
import numpy as np
print(np.triu(result))
[[ 0.       41.666667 16.666667 70.37037 ]
 [ 0.        0.       58.333333 33.333333]
 [ 0.        0.        0.       62.962963]
 [ 0.        0.        0.        0.      ]]
```
Or we can print the data as condensed matrix using scipy:

```python
import scipy.spatial.distance as ssd
result = ssd.squareform(result)
print(result)
[41.666667 16.666667 70.37037  58.333333 33.333333 62.962963]
```

This can be used, for instance, as input to scipy hierarchical clustering algorithms: 

```python
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(result, method='ward'), labels = names, leaf_font_size= 10, orientation = 'top',
                      color_threshold = 2, leaf_rotation=45)
plt.show()
```
![image](https://user-images.githubusercontent.com/79587588/114025796-3193c080-987e-11eb-84c5-fb224ca04662.png)

