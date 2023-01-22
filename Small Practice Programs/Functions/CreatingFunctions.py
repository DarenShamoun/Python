#Flesh out the body of the print_seconds function so that it prints 
# the total amount of seconds given the hours, minutes, 
# and seconds function parameters. 
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    print((hours * 3600) + (minutes * 60) + seconds)

print_seconds(1,2,3)

# We start a function definition with the def keyword, 
# followed by the name we want to give our function. 
# After the name, we have the parameters, also called arguments, 
# for the function enclosed in parentheses. 
# A function can have no parameters, or it can have multiple parameters. 
# Parameters allow us to call a function and pass it data, 
# with the data being available inside the function as 
# variables with the same name as the parameters. Lastly, 
# we put a colon at the end of the line.

# After the colon, the function body starts. 
# It’s important to note that in Python the function 
# body is delimited by indentation. 
# This means that all code indented to the right following 
# a function definition is part of the function body. 
# The first line that’s no longer indented is the 
# boundary of the function body. 
# It’s up to you how many spaces you use 
# when indenting -- just make sure to be consistent. 
# So if you choose to indent with four spaces, 
# you need to use four spaces everywhere in your code.