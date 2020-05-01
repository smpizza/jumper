# Lab 5 Random Emoticon Generator
import random

# List
eyes = ["0  0", "^  ^", "-  -", "0  -", "=  =", ".  .", "-  0"]
noses = [" |", "  ", " ^", " 0", " L"]
mouths = ["---", "~~~", "===" ]

# Face generator
print("Let's make a face!")
print()
eye = random.choice(eyes)
print(eye)
nose = random.choice(noses)
print(nose)
mouth = random.choice(mouths)
print(mouth)

# Loop

while True:
    ask = input("Make Another Face? yes or no ")
    if ask == "no":
        print("okay, goodbye!")
        break
    elif ask == "yes":
        print("Let's make a face!")
        print()
        eye = random.choice(eyes)
        print(eye)
        nose = random.choice(noses)
        print(nose)
        mouth = random.choice(mouths)
        print(mouth)
