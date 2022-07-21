#PyPi - Python Package Index, a bunch of software share by Python community
# Documents: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Type", ["Fire", "Water", "Grass"])

# change Attributes of table, its style
table.align = "l" #align the column to the left
print(table)
