# notes from saturday Feb 22

#####################
# NUMPY
#####################

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

#####################
# PANDAS
#####################

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


# pandas activities

# I
# average of first 100 rows 
df['PRICE'][:100].mean()

df['CHAS'][:100].mean()
'''
0.0
'''

# average of first 100 rows B and CHAS columns
df[['B', 'CHAS']][:100].mean()
'''
    B       385.3015
    CHAS      0.0000
    dtype: float64
'''

# mean of first 50 rows for columns with index positions 0 and 1
df.iloc[:50, [0, 2]].median()
'''
    CRIM     0.22233
    INDUS    7.87000
    dtype: float64
'''
# confirm
df['CRIM'][:50].median()
'''
    0.22233
'''
df['INDUS'][:50].median()
'''
    7.87
'''


# II
# multiple conditions
df[(df['RM'] > 7) & (df['TAX'] < 300)]

# average price when taxes above 300
df[df['TAX'] > 300]['PRICE'].mean()

# average praice when taxes > 300 and chas = 1
df[(df['TAX'] > 300) & (df['CHAS'] == 0)]['PRICE'].mean()

# number of houses with crime over average and chas = 1
average = df['CRIM'].mean()
df[(df['CHAS'] == 0) & (df['CRIM'] > average)]


#####################
# charts (seaborn graphic library)
#####################
import seaborn as sns
import matplotlib as plt

df.head()
sns.regplot(x = 'RM', y = 'PRICE', data = df)

sns.distplot(df['PRICE'])
# save image
plt.savefig('hist.png')


#####################
# MACHINE LEARNING 
#####################

from sklearn.linear_model import LinearRegression

lreg = LinearRegression()
lreg
'''
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
'''

x = df[['RM', 'LSTAT']]
y = df['PRICE']

# fit
lreg.fit(x, y)
'''
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False) 
'''

# m slope: first number RM (m1) second - LSAT (m2)
lreg.coef_
'''
    array([ 5.09478798, -0.64235833])
'''

# b intercept
lreg.intercept_
'''
    -1.3582728118744818
'''

# score 
lreg.score(x, y)
'''
    0.6385616062603403
'''

# predict - using y = mx + b formula
lreg.predict(x)
'''
    array([28.94101368, 25.48420566, 32.65907477, 32.40652   , 31.63040699,
           28.05452701, 21.28707846, 17.78559653,  8.10469338, 18.24650673,
           17.99496223, 20.73221309, 18.5534842 , 23.64474107, 23.10895823,
           22.9239452 , 24.65257604, 19.73611045, 18.9297215 , 20.57377596,
           13.51732408, 20.14832175, 17.90896697, 15.48764606, 18.35281036,
           16.56210901, 18.74440281, 18.34995811, 23.51018847, 24.94888935,
    ...
'''

# exercise
X = df.iloc[:, :-1]
y = df['PRICE']

lreg.fit(X, y)

lreg.coef_
'''
    array([-1.08011358e-01,  4.64204584e-02,  2.05586264e-02,  2.68673382e+00,
       -1.77666112e+01,  3.80986521e+00,  6.92224640e-04, -1.47556685e+00,
        3.06049479e-01, -1.23345939e-02, -9.52747232e-01,  9.31168327e-03,
       -5.24758378e-01])
'''

lreg.intercept_
'''
    36.459488385090005
'''

lreg.score(X, y)
'''
    0.7406426641094094
'''

###

coeffs = {
    'Column' : X.columns,
    'Coeff' : lreg.coef_
}

coeffs
'''
    {'Column': Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
            'PTRATIO', 'B', 'LSTAT'],
        dtype='object'),
    'Coeff': array([-1.08011358e-01,  4.64204584e-02,  2.05586264e-02,  2.68673382e+00,
            -1.77666112e+01,  3.80986521e+00,  6.92224640e-04, -1.47556685e+00,
            3.06049479e-01, -1.23345939e-02, -9.52747232e-01,  9.31168327e-03,
            -5.24758378e-01])}
'''

coef_df = pd.DataFrame(coeffs)
coef_df.sort_values(by = 'Coeff', ascending = False)
'''
        Column	Coeff
    5	RM	    3.809865
    3	CHAS	2.686734
    8	RAD	    0.306049
    1	ZN	    0.046420
    2	INDUS	0.020559
    11	B	    0.009312
    6	AGE	    0.000692
    9	TAX	    -0.012335
    0	CRIM	-0.108011
    12	LSTAT	-0.524758
    10	PTRATIO	-0.952747
    7	DIS	    -1.475567
    4	NOX	    -17.766611
'''

df['NOX'].max()
'''
    0.871
'''

df['NOX'].min()
'''
    0.385
'''

# resize the data / scale: STANDARDIZATION
X-X.mean()
'''
    0	-3.607204	6.636364	-8.826779	-0.06917	-0.016695	0.290366	-3.374901	0.294957	-8.549407	-112.237154	-3.155534	40.225968	-7.673063
    1	-3.586214	-11.363636	-4.066779	-0.06917	-0.085695	0.136366	10.325099	1.172057	-7.549407	-166.237154	-0.655534	40.225968	-3.513063
    2	-3.586234	-11.363636	-4.066779	-0.06917	-0.085695	0.900366	-7.474901	1.172057	-7.549407	-166.237154	-0.655534	36.155968	-8.623063
    3	-3.581154	-11.363636	-8.956779	-0.06917	-0.096695	0.713366	-22.774901	2.267157	-6.549407	-186.237154	0.244466	37.955968	-9.713063
    4	-3.544474	-11.363636	-8.956779	-0.06917	-0.096695	0.862366	-14.374901	2.267157	-6.549407	-186.237154	0.244466	40.225968	-7.323063
    ...	...	...	...	...	...	...	...	...	...	...	...	...	...
'''

X.describe()
X = X / X.std()
X.describe()
'''
    std is now 1
'''

# exercise on standardized set

lreg.fit(X, y)
lreg.score(X, y)
'''
    same as before
'''

coeffs = {
    'Column' : X.columns,
    'Coeff' : lreg.coef_
}

coeffs
'''
    {'Column': Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
            'PTRATIO', 'B', 'LSTAT'],
        dtype='object'),
    'Coeff': array([-0.92906457,  1.08263896,  0.14103943,  0.68241438, -2.05875361,
            2.67687661,  0.01948534, -3.10711605,  2.6648522 , -2.07883689,
            -2.06264585,  0.85010886, -3.74733185])}
'''

coef_df = pd.DataFrame(coeffs)
coef_df.sort_values(by = 'Coeff', ascending = False)
'''
        Column	Coeff
    5	RM	    2.676877
    8	RAD	    2.664852
    1	ZN	    1.082639
    11	B	    0.850109
    3	CHAS	0.682414
    2	INDUS	0.141039
    6	AGE	    0.019485
    0	CRIM	-0.929065
    4	NOX	    -2.058754
    10	PTRATIO	-2.062646
    9	TAX	    -2.078837
    7	DIS	    -3.107116
    12	LSTAT	-3.747332
'''

# shapes for these graphs are identical. 
# when standardize, you change scale. 
df['TAX'].hist()
X['TAX'].hist()