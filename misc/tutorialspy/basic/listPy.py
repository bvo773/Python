# (Datatype) List -  A container that stores ordered sequence of objects(values). Can be modified. 
# listName = [object1, object2, object3]

def printFruits(fruits):
    for fruit in fruits:
        print(fruit)
    print("\n")

fruits = ["Apple", "Orange", "Strawberry"]
fruits[0] #Accessing a list
fruits[1] = "Mango" #Modifying a list 
fruits.append("Kiwi") #Adding an element the 'end' of the list
fruits.insert(1,"Banana") # Insert an element at certain index
fruits.remove("Strawberry")
printFruits(fruits)

fruits.sort()
printFruits(fruits)



    
