#Lab2 Mad Lib

message = "Let's play a game!"
print(message)
adj1 = input("First, give me an adjective to describe your height: ")
veg = input("Now name a vegetable: ")
noun1 = input("Now give me a noun: ")
noun2 = input("And another noun: ")
verb = input("Now, give me a verb past tense: ")
noun3 = input("Finally, name a special place: ")

# madlib story
madlib=f"""
Today I went to the zoo. I saw a {adj1} {veg} jumping up and down in its {noun1}.
He {verb} through the large {noun2} that led to its {noun3}.
"""
print(madlib)