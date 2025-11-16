
family = {
    "husband": {
        "name" : "john doe",
        "age" : 32
    },

    "wife": {
        "name": "jane doe",
        "age": 31
    },

    "son" : {
        "name" : "jim doe",
        "age": 6
    }
}

print(family["husband"]["name"])

child1 = {
    "name": "Anthony"
}

child2 = {
    "name" : "Shay"
}

child3 = {
    "name" : "Hali"
}

parentDict = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(parentDict["child1"]["name"])

for x, obj in family.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])