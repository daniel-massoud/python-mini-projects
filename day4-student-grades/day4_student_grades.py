def addStudent(gradeDict, name, grade):
  gradeDict[name] = grade

def calculateAverage(gradeDict):
  total = 0
  for grade in gradeDict.values():
    total += grade
  if len(gradeDict) > 0:
     return total / len(gradeDict)
  else :
    return 0

#main program
gradeDict = {}
numStudents = int(input("enter number of students:"))
for i in range(numStudents):
  try:
    name = input("enter student name:")
    grade = float(input("enter student grade:"))
    addStudent(gradeDict, name.lower(), grade)
  except ValueError:
    print("invalid grade")

#summary of the results 
print("summary of the results:")
for name, grade in gradeDict.items():
  print(f"{name}: {grade}")

average = calculateAverage(gradeDict)
print(f"average grade: {average}")

