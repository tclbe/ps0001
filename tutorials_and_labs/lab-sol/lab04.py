#%% Task 1
import random

w = random.randint(1, 100)
x = int(input("Enter a number between 1 and 100: "))
diff = abs(x - w)

if diff <= 5:
    print("You win a large prize!")
elif diff <= 10:
    print("You win a small prize.")
else:
    print("You lost :(")
print("The winning number was ", w, ".", sep="")

#%% Task 1 no abs
import random

w = random.randint(1, 100)
x = int(input("Enter a number between 1 and 100: "))
diff = x - w

if -5 <= diff <= 5:
    print("You win a large prize!")
elif -10 <= diff <= 10:
    # elif -10 <= diff < -5 or 5 < diff <= 10:
    print("You win a small prize.")
else:
    print("You lost :(")
print("The winning number was ", w, ".", sep="")

#%% Task 2
print("The Decision Maker Assistant Program")
print("Enter two options to decide between.")
opt1 = input("Option 1: ")
opt2 = input("Option 2: ")
p = input("% probability of choosing option 1 (defaults to 50%): ")

# Handle user input.
if p != "":
    p = float(p)
    p /= 100
else:
    p = 0.5

# Make the decision.
rando = random.random()
print("Random number generated:", rando)
print("Probability of choosing option 1:", p)
if rando < p:
    print("You should", opt1)
else:
    print("You should", opt2)
