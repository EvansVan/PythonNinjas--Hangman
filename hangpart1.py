import random

scrabblebook = open('sowpods.txt')

words = scrabblebook.readlines()

randomWord = random.choice(words)

#my test to confirm i have correct file
print(words[0])

print(randomWord)

#my test to confirm i have correct file
print(len(words))
