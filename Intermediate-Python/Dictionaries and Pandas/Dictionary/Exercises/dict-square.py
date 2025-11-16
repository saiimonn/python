n = int(input("Enter n: "))
dict = {}

for i in range(1, 5 + 1):
    dict.update({i : i * i})

print(dict)