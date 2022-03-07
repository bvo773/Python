'''
101 - [Interactive Coding Exercise
Taking the year and month inputs, output how many days are in a month given a year and month
'''
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(num_year, num_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month > 12 or month < 1:
    return "Invalid year or month"
  if is_leap(num_year):
    total_day = month_days[num_month-1] + 1
    return total_day
  return month_days[num_month-1]
  
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

