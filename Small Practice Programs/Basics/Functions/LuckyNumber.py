def lucky_number(name):
  number = len(name) * 9
  editedNumber = "Hello " + name + ". Your lucky number is " + str(number)
  return editedNumber
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))