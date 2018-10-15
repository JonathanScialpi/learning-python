last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Create a list called subjects and fill it with the classes you are taking
subjects = ["physics", "calculus", "poetry", "history"]

#Create a list called grades and fill it with your scores
grades = [98,97,85,88]
subjects.append("computer science")
grades.append(100)

# Use the zip() function to combine subjects and grades
gradebook = list(zip(subjects,grades))
gradebook.append(("visual arts", 93))

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)