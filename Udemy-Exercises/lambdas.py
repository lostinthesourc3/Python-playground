# lambdas 
# 1
cube = lambda num: num ** 3

# 2
def decrement_list(l):
    return list(map(lambda n: n-1, l))

# 3
def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))

# 4
def is_all_strings(lst):
    return all(type(l) == str for l in lst)

# 5
def extremes(nums):
    return(min(nums), max(nums))

# 6
def max_magnitude(nums):
    return max(abs(num) for num in nums)

# 7
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

# 8
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

# 9
