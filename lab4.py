
# Lab 4 Grading
import random

# 90 to 100 percentile
num = int(input("enter a number: "))
if num >= 90 and num <= 100:
    print("Congratulations! You got a 'A'")
    print("you're rival scored...")
    print(random.randint(70,80))

# 80 to 89 percentile
elif num >= 80 and num <= 89:
    print("Great job! You got a 'B'")
    print("you're rival scored...")
    print(random.randint(90,100))

# 70 to 79 percentile
elif num >= 70 and num <= 79:
    print("Nice! You got a 'C'")
    print("you're rival scored...")
    print(random.randint(80,100))

# 60 to 69 percentile
elif num >= 60 and num <= 69:
    print("Well, at least you got a 'D'")
    print("you're rival scored...")
    print(random.randint(90,100))

# 0 to 59 percentile
elif num >= 0 and num <= 59:
    print("Yikes you didn't pass, but you're still cool!")
    print("you're rival scored...")
    print(random.randint(60,100))