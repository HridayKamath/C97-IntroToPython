from itertools import count
from re import I


description = input("Write a few words on yourself:")
print(description)
characterCount = 0
wordCount = 1
for character in description:
    characterCount = characterCount + 1
    if(character == " "):
        wordCount = wordCount + 1
print(characterCount)
print(wordCount)
