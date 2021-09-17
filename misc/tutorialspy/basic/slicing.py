# Slicing a list
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         0  1  2  3  4  5  6  7  8  9
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print (myList[-1])  # Prints the last value in the list
print (myList[0:5]) # list[start:end] end non-inclusive
print (myList[:-2]) # 0.....7
print (myList[1:])  # 1.....9
print (myList[0:9:2]) # list[start:end:step] 0..2..4..6..8 skip a value with step = 2
print (myList[-1:2:-1]) # print in reverse without skipping

# Slicing a string
sampleUrl = 'http://trashbin.net'
print (sampleUrl)

# Reverse the URL
print (sampleUrl[::-1])

# Get the top level domain
print (sampleUrl[-4:])

# Print the Url without the http://
print (sampleUrl[7:])

# Print the Url without the http:// or the top level domain
print (sampleUrl[7:-4])