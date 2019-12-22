age = input("Enter your age: ")

if age:
    age = int(age)
    if age >= 21:
        print("You can enter and can drink")
    elif age >= 18:
        print("You can come in, but you can't drink")
    else: 
        print("you can't come in little one!")
else:
    print("Please, enter your age")