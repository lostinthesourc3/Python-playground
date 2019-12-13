# for
for n in range(1, 11):
    print("👽" * n)

# while
n = 1
while n <= 10:
    print("👽" * n)
    n += 1

# nested
for n in range(1, 11):
    count = 1
    symbol = ""
    while count <= n:
        symbol += "*"
        count += 1
    print(symbol)