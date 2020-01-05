# functions exercises

# 1
def make_noise():
    print("THE CROWD GOES WILD")
make_noise()

# 2
def speak_pig():
    return 'oink'

# 3
def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

# 4
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

# 5
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

# 6
def product(a,b):
    return a*b

# 7
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

# 8
def last_element(l):
    if l:
        return l[-1]
    return None

# 9
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

# 10
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

# 11
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# 12
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

# 13
def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

# 14
def frequency(collection, searchTerm):
    return collection.count(searchTerm)

# 15
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

# 16
def capitalize(string):
    return string[:1].upper() + string[1:]

# 17
def compact(l):
    return [val for val in l if val]

# 18
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

# 19
def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

# 20
def contains_purple(*args):
    if "purple" in args: return True
    return False

# 21
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

# 22
def count_sevens(*args):
    return args.count(7)
 
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
result1 = count_sevens(1,4,7)
result2 = count_sevens(*nums)
