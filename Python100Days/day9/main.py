'''
DAY 9 - DICTIONARIES, NESTING, SECRET SILENT AUNCTION TERMINAL
'''

'''
91 PYTHON DICTIONARY DEEP DIVE
Python dictionary is like a dictionary in real life

key : value
word : definition
code : programs instructions

Dictionaries are useful because they allow us to group together 
and tag related pieces of information.

If you want to add more entry in your dictionary. Separate each of the key value pairs
using a comma. You can add your key value pairs until the dictionary ends
Syntax:
{Key : Value}

{
  "Bug" : "An error in a programs that prevents the program from running as expected.",
  "Function" : "A piece of code that you can easily call over and over again.",
  "Loop" : "The action of doing something over and over again.",
}
'''

programming_dictionary = {
  "Bug" : "An error in a programs that prevents the program from running as expected.",
  "Function" : "A piece of code that you can easily call over and over again.",
}

# RETRIEVING items from dictionary, use the key, in this case  the key is a String
# Make sure the key is spell correctly, case sensitive or will KeyError exception
print(programming_dictionary["Bug"])

# ADDING new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#CREATE an empty dictionary
empty_dictionary = {}
empty_dictionary["Yahweh"] = "The god of the Israelites and Gentiles in biblical Scripture"

# Clear an existing dictionary, completely empty
# programming_dictionary = {}
# print(programming_dictionary)

# EDIT an item in the dictionary
# Finds a value with this key and then assign it to whatever put on the right
# If it finds nothing with that key, it will create a new entry with the assign value
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# LOOP through a dictionary, iterable is the key
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key]) #use the key to print out the value

