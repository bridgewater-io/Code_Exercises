# Magic 8-Ball project
# Imports the random module as part of the standard Python library
import random

# Change the name variable below if you want it personalized to your name
name = "notACat"

# Change the question variable below for a personalized non-default question
question = "Can cats have cheeseburgers?"

# Do not change logic below this block

answer = "" # Variable to hold the answer, blank string on initialization

# Random number to be generated from the random module imported, imports a number between 1 (inclusive) and 9 (inclusive)
random_number = random.randint(1,11)

# Test output to ensure random_number is working as intended print(random_number)

# if/elif/else statement to provide a value for the answer variable
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "What kind of question is that?!"
elif random_number == 11:
  answer = "100%, now and always."
else:
  answer = "Error"

# Output block with optional challenges
# Checks the question variable first as the script relies on a question
if question == "":
  print("You must first ask a question.")
elif name == "":
  print(f"Question: {question}")
  print(f"Magic 8-Ball's answer: {answer}")
else:
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer: {answer}")

  




