# students = ["Hermione", "Harry", "Ron", "Draco"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#   "Hermione": "Gryffindor",
#   "Harry": "Gryffindor",
#   "Ron": "Gryffindor",
#   "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student])


students = [
  { "name": "Hermione", "house": "Gryffindor", "patronus": "Otter" },
  { "name": "Harry", "house": "Gryffindor", "patronus": "Stag" },
  { "name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier" },
  { "name": "Draco", "house": "Gryffindor", "patronus": None },
]

for student in students: # student is a dictionary
  print(student["name"], student["house"], student["patronus"], sep=", ") # For each student in our list of students, print out their name, house, and patronus