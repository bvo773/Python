'''
93 - NESTING DICTIONARIES and LISTS to store more complex pieces of data
{
  Key : [List],
  key3 : {Dict},
}
'''
# Sample Simple Dictionary
# key: country | value: capital cities
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# A Travel log to collect a dictionary of all the cities been through to represent more complex data.
# Instead of having 1 value for each key, we can nest a Dictionary or List to represent more values or complex data.
# NESTING a DICTIONARY in a Dictionary
# NESTING a LIST in a Dictionary
# NESTING a DICTIONARY in a Dictionary
# Storing cities for each visited country, each country
# has a value of a dictionary within itself
travel_log = {
  "France": {"cities_visited": ["Paris","Lille","Dijon" ], "total_visits": 10},
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
  "Vietnam": {"cities_visited": ["Da Nang", "Hoi An", "Saigon"], "total_visits": 3},
}

'''
NESTING A DICTIONARY INSIDE A LIST, we can have multiple dictioanries inside a list
[{
  Key: [List],
  Key2: {Dict},
},
{
  Key: Value,
  Key2: Value,
}]
'''
travel_log = [
  {
    "country": "France", 
    "cities_visited": ["Paris","Lille","Dijon" ], 
    "total_visits": 10
  },
  {
    "country": "Germany", 
    "cities_visited":  ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 2
  },
  {
    "country": "Vietnam",
    "cities_visited": ["Da Nang", "Hoi An", "Saigon"], 
    "total_visits": 3
  },
]
