
# sentence = "apple banana apple orange banana apple"
sentence = str(input())
newSentence = sentence.split()

dict = {}

for y in newSentence:
    if y not in dict:
        count = 1
        dict.update({y : count})
    else:
        dict[y] += 1

print(dict)