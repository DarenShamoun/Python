# The guest_list function reads in a list of tuples with the name, 
# age, and profession of each party guest, and prints the sentence 
# "Guest is X years old and works as __." for each one. For example, 
# guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), 
# ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old 
# and works as Chef. Pat is 35 years old and works as Lawyer. 
# Amanda is 25 years old and works as Engineer.

def guest_list(guests):
	for person in guests:
		name , age, profession = person
		print("{} is {} years old and works as a {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""