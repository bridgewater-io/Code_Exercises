# 11/19/26

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Step 1: Creating a list of subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Step 2: Creating a list of grades
grades = [98, 97, 85, 88]

# Step 3: Combining subjects and grades manually to create a 2D-List to simulate a gradebook
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

# Step 4: Test output
print(f"Step 4 Output: {gradebook}")

# Step 5 and 6: Using list methods to add values to the gradebook
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Step 7, 8, and 9: Modifying existing values in the gradebook using list methods
gradebook[-1][-1] += 5
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Step 10: Creating the final gradebook combining last semesters grades
full_gradebook = last_semester_gradebook + gradebook 

# Final Output
print(f"\nFull Gradebook: {full_gradebook}")

