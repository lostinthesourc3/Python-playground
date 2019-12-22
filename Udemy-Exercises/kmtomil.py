print("How many km did you drive today?")
km = input()
mil = float(km)/1.61
mil = round(mil, 2)
print(f"You drove {km} kilometers, which is {mil} miles")