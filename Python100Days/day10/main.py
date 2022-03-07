'''
DAY 10 - FUNCTIONS WITH OUTPUTS
'''

'''
99 - Functions with Outputs, output keyword 'return' to output result
BINH VO - Binh Vo
biNH vO - Binh Vo
Title Case in Python - string.title() - word start out with a capital letter

def my_function():
  result = 3 * 2
  return result

'''
def format_name(f_name, l_name):
  full_name = f_name.title() + " " + l_name.title()
  return full_name


'''
100 - Multiple values return, function will terminate when it sees the first return
102 - DOCSTRINGS - Between the 3 quotations part if where you can write your function documentation - """ """

Will return 'None' below since there is no output to print
'''
def format_name_2(f_name, l_name):
  """Take first and last name and format it to return 
  the title case version of the name."""
  
  if f_name == "" or l_name == "":
    return
  return f"{f_name.title()} {l_name.title()}"

print(format_name_2(input("What is your first name? "), input("What is your last name? ")))

