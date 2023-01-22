# the student_grade function using the format method, 
# so that it returns the phrase "X received Y% on the exam". 
# For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	return ("{name} received {grade}% on the exam".format(name = name, grade = grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))