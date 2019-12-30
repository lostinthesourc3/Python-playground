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
