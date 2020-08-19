import os, pprint
os.system('cls')

message = input("Enter a string: ")
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)