name1 = input("What is your name? ")
height1 = int(input("what is your height? "))
name2 = input("What is your name? ")
height2 = int(input("what is your height? "))
name3 = input("What is your name? ")
height3 = int(input("what is your height? "))

if height1 > height2:
    print(name1 + " is the tallest")
elif height2 > height3:
    print(name2 + " is the tallest")
else:
    print(name3 + " is the tallest") 