import random

target = random.randint(1, 100)

while True:
    userchoise = input("Guess the target or quit(Q) : ")
    if userchoise == "Q":
        break

    userchoise = int(userchoise)
    if userchoise == target:
        print("Success : Correct Guess")
        break
    elif userchoise < target:
        print("Your number was too small. take a bigger guess..")
    else:
        print("Your number was to big. Take a smaller guess..")

print("----Game Over----")