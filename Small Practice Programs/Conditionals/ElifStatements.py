# The number_group function should return "Positive" 
# if the number received is positive, "Negative" 
# if it's negative, and "Zero" if it's 0.

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative