# Project : Quiz Game

print("Welcome to Computer Quiz Game!")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! \n")
score = 0

# Question 1
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


# Question 2
answer = input("What does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


# Question 3
answer = input("What does SPU stands for? ")
if answer.lower() == "supply power unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


# Question 4
answer = input("What does SU stands for? ")
if answer.lower() == "system unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


# Percentage
percentage = ((score/4)*100)

# Output using newer string formatting
print(f"You got {score} questions correct!")
print(f"You got {percentage}%")
