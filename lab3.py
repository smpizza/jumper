# Lab 3 Magic Eight Ball
import random
# list of predictions
predictions = ["lets talk about something else", "you're crazy, but I like you", "when pigs fly", "you're totally screwed", "take the money and run"]

# welcome message
print("Welcome to the Magic Eight Ball!")
name = input("What's your name?")
print("hello" + " " + name)

# user input
while True:
  answer = input("Do you want to play? yes or no: ")
  if answer.lower() == "yes":
    print("Muahahaha!")
    quest1 = input("Well, aren't you a brave one. Press enter to continue. ")
    quest2 = input("Ask me anything, for I see all! ")
    message = random.choice(predictions)
    print(message)
  else:
    print("you're no fun.")