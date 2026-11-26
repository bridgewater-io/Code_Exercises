python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics) # First creating a list to count the end condition for the while loop

index = 0 # Second, creating a counter to compare to the length of the list in order to have a condition to complete the while loop

while index < length:
  print(f"I am learning about {python_topics[index]}") # This will find the index position of the python_topics list at each iteration and print them one by one
  index += 1
