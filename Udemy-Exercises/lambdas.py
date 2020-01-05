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
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

# 10
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

# 11
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

