# Using the format() method
#   The format method returns a copy of the string where the 
#   {} placeholders have been replaced with the values of the variables. 
#   These variables are converted to strings if they weren't strings already. 
#   Empty placeholders are replaced by the variables passed to format in the same order.
#   EX:
"""  # "base string with {} placeholders".format(variables)

      example = "format() method"

      formatted_string = "this is an example of using the {} on a string".format(example)

      print(formatted_string) 
"""

""" Outputs:
    "this is an example of using the format() method on a string"
"""

# If the placeholders indicate a number, they’re replaced by the 
# variable corresponding to that order (starting at zero).
#   EX:
"""   # "{0} {1}".format(first, second)

      first = "apple"
      second = "banana"
      third = "carrot"

      formatted_string = "{0} {2} {1}".format(first, second, third)

      print(formatted_string)
"""
"""     Outputs:
        "apple carrot banana" 
"""
    

# If the placeholders indicate a field name, they’re replaced 
# by the variable corresponding to that field name. 
# This means that parameters to format need to be passed indicating the field name.

""" EX: # "{var1} {var2}".format(var1=value1, var2=value2) """

# If the placeholders include a colon, 
# what comes after the colon is a formatting expression. 
# See below for the expression reference.

""" #{:d} integer value
    '{:d}'.format(10.5) → '10' 
"""

# Formatting expressions

"Expr"	"Meaning"	"Example"
# {:d}	    integer value	'{:d}'.format(10.5) → '10'
# {:.2f}	floating point with that many decimals	    '{:.2f}'.format(0.5) → '0.50'
# {:.2s}	string with that many characters	'{:.2s}'.format('Python') → 'Py'
# {:<6s}	string aligned to the left that many spaces	    '{:<6s}'.format('Py') → 'Py    '
# {:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
# {:^6s}	string centered in that many spaces	    '{:^6s}'.format('Py') → '  Py  '