'''
DAY 13 - Debugging - The process of removing bugs from our code

Everyone get bugs. 

Top TIPS to help debugging below
'''

############DEBUGGING#####################

# Describe Problem - i never == 20, increase range from 20 to 21
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug - index out of range
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer - Pretend to be a computer going through each line of vcode
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors - If console give errors, fix errors before continuing
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend - Your best friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# #Use a Debugger - If print doesnt work, debugger is your best friend pythontutor
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Take a Break - Dont stare at the code, have a nap, go to sleep, tackle it tomrrow, if you get stuck, ask a friend.
# Run often - Run your code often
# Ask Stackoverflow