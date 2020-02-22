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

