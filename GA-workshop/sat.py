# notes from saturday Feb 22
# NUMPY
import numpy as np

arr = np.arange(20).reshape(5, 4)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15],
#        [16, 17, 18, 19]])

arr.mean()
# 9.5

arr.mean(axis = 0)
# returns mean row
# array([ 8.,  9., 10., 11.])

arr.mean(axis = 1)
# mean of each row
# array([ 1.5,  5.5,  9.5, 13.5, 17.5])


# PANDAS
import pandas as pd

# import file, save as variable
df = pd.read_csv("/Users/yuli/Desktop/housing.csv")

# change how many rows it shows
# pd.set_option('max_rows', 20)

# select a column
df['CRIM']
'''
    0      0.00632
    1      0.02731
    2      0.02729
    3      0.03237
    4      0.06905
            ...   
    501    0.06263
    502    0.04527
    503    0.06076
    504    0.10959
    505    0.04741
    Name: CRIM, Length: 506, dtype: float64
'''

# select multiple columns
# passed in as a list
df[['CRIM', 'NOX', 'RM']]
'''
    	CRIM	NOX	    RM
    0	0.00632	0.538	6.575
    1	0.02731	0.469	6.421
    2	0.02729	0.469	7.185
    3	0.03237	0.458	6.998
    4	0.06905	0.458	7.147
    ...	...	...	...
    501	0.06263	0.573	6.593
    502	0.04527	0.573	6.120
    503	0.06076	0.573	6.976
    504	0.10959	0.573	6.794
    505	0.04741	0.573	6.030
    506 rows × 3 columns
'''

# slice across rows
# select forst 50 rows (slice 50 rows)
df[['NOX', 'RM']][:50]

# slice from 40 to 50 
df[['NOX', 'RM']][40:50]

# slice across columns
# this grabs every row, column 2 through 6
df.iloc[:, 2:6]

# this grabs rowns 5-11, columns 2-6
df.iloc[5:11, 2:6]
'''
        INDUS	CHAS	NOX	    RM
    5	2.18	0	    0.458	6.430
    6	7.87	0	    0.524	6.012
    7	7.87	0	    0.524	6.172
    8	7.87	0	    0.524	5.631
    9	7.87	0	    0.524	6.004
    10	7.87	0	    0.524	6.377
'''

# get specific columns
df.iloc[5:11, [0, 2, 4, 9]]


