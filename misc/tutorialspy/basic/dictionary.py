# A Dictionary is a set(collection) of key-value pairs, similar to a List. Instead of accessing it by an integer index, you'll use a 'key' as an index.
# Use a dictionary when you want your value to be associated with a particular key
# dictionaryName = {key1: value1, key2, value2}

# Dictionary to map the price of a camera to its brand
priceOfCameras = {"sony": 500, "nikon": 600, "canon": 700}
priceOfCameras["sony"] = 400 # Retreiving and Modifying its value by its key

# Operations that can be performed on Dictionary #
print (priceOfCameras.keys()) # Get all of the keys [dictionary.keys()]
print (priceOfCameras.values()) # Get all of the values [dictionary.values()]

copyOfPriceOfCameras = priceOfCameras.copy() # Copy one dictionary to another [dictionary.copy()]
del(copyOfPriceOfCameras["sony"]) # Delete a key-value pair from a dictionary
print(copyOfPriceOfCameras)
copyOfPriceOfCameras.clear() # Clearing a dictionary 


