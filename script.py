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
