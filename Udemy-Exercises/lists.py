# lists basics

my_stuff = [1, 2, 3, 4, "cat", 0.333]
nums = list(range(1,10))


people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"


sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()


instructors = [] #append names
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")

new_instructors = []
new_instructors.extend(["Colt", "Blue", "Lisa"])
# Remove the last value in the list
new_instructors.pop()
# Remove the first value in the list
new_instructors.pop(0)
# Add the string "Done" to the beginning of the list
new_instructors.insert(0, "Done")


