def grade_converter(gpa):
  if gpa >= 4:
    grade = "A"
  elif gpa >= 3:
    grade = "B"
  elif gpa >= 2:
    grade = "C"
  elif gpa >= 1:
    grade = "D"
  elif gpa >= 0:
    grade = "F"
  return grade  
  
print(grade_converter(0.6))

Astar = 40
A = 37
B = 30
C = 20
D = 10
E = 0

# 4.0 > 120. Once student enters these grades they will convert to a value


def brit_converter(grade1, grade2, grade3):
  sum = grade1 + grade2 + grade3:
   if sum >= 120:
    grade = 4.0
  elif sum >= 100:
    grade = "3.0"
  elif sum >= 80:
    grade = "2.0"
  elif sum >= 60:
    grade = "1.0"
  elif sum >= 0:
    grade = "Did not pass"
  return grade  
