## While Loops
    # A while loop executes the body of the loop while the condition remains True.
    # Syntax:
"""     while condition:
            body            """
# Things to watch out for!
    # Failure to initialize variables. Make sure all the variables 
    # used in the loop’s condition are initialized before the loop.
    # Unintended infinite loops. Make sure that the body of the loop modifies 
    # the variables used in the condition, so that the loop will eventually 
    # end for all possible values of the variables.
# Typical use:
# While loops are mostly used when there’s an unknown number of operations 
# to be performed, and a condition needs to be checked at each iteration.


## For Loops
    # A for loop iterates over a sequence of elements, 
    # executing the body of the loop for each element in the sequence.
    # Syntax:
"""     for variable in sequence
            body            """


## The range() function:
    # range() generates a sequence of integer numbers. 
    # It can take one, two, or three parameters:
"""     range(n): 0, 1, 2, ... n-1
        range(x,y): x, x+1, x+2, ... y-1
        range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment) """


# Recursive functions
#   A recursive function must include a recursive case and base case. 
#   The recursive case calls the function again, with a different value. 
#   The base case returns a value without calling the same function.
    # A recursive function will usually have this structure:
"""     def recursive_function(parameters):
            if base_case_condition(parameters):
                return base_case_value
            recursive_function(modified_parameters) """


# Break & Continue
#   You can interrupt both while and for loops using the "break" keyword. 
#   We normally do this to interrupt a cycle due to a separate condition.
#   You can use the "continue" keyword to skip the current iteration 
#   and continue with the next one. This is typically used to jump 
#   ahead when some of the elements of the sequence aren’t relevant.