'''
Caesar Cipher is a way of encoding text. 
Julius Cesar would shift each letter of the alphabet by a certain
a predetermined amounts.

Shift = 0
A B C D E F G
| | | | | | |
A B C D E F G

Shift = 1
A B C D E F G
| | | | | | |
B C D E F G H

Shift = 2
A B C D E F G
| | | | | | |
C D E F G H I

Shift = 2
A B C D E F G
| | | | | | |
D E F G H I J

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
'''


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0','1', '2', '3', '4', '5', '6','7','8','9']
punctuation = ['.', ',', '?', '!',':', ';']
symbols = ['@','$','#','%','/', '|', '>','<','=','(',')','-','+']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plainText, shiftAmount):
  # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
  cipherText = ""
  for letter in plainText:
    if letter == " ":
      cipherText += " "
    elif letter in punctuation or letter in nums or letter in symbols:
      cipherText += letter
    else:
      position = alphabet.index(letter)
      #There's no need to check if it's > 25, as any number below 26 if modulo-ed with 26 is itself.
      #(Using len(alphabet) instead of assuming 26 would, of course, be more correct to handle other alphabets!)
      newPosition = (position + shiftAmount) % len(alphabet) 
      cipherText += alphabet[newPosition]
    
  print(f"Here is your ENCRYPTED Text:\n ->{cipherText}")

def decrypt(cipherText, shiftAmount):
  plainText = ""
  for letter in cipherText:
    if letter == " ":
      plainText += " "
    elif letter in punctuation or letter in nums or letter in symbols:
      plainText += letter
    else:
      position = alphabet.index(letter)
      #There's no need to check if it's < -1, as any number below 26 if modulo-ed with 26 is itselt.
      # If it is negative, -x + len(arr)
      #(Using len(alphabet) instead of assuming 26 would, of course, be more correct to handle other alphabets!)
      newPosition = (position - shiftAmount) % len(alphabet)
      plainText += alphabet[newPosition]
    
  print(f"Here is the DECRYPTED Text:\n ->{plainText}")

# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
from caesar_logo_ascii import logo
print(logo)
endEncoding = False
while not endEncoding:
  direction = input("Type 'encode' or '1' to encrypt, type 'decode' or '2' to decrypt:\n ->")

  if direction == "encode" or direction == "1":
    text = input("Type your message:\n ->").lower()
    shift = int(input("Type the shift number:\n ->"))
    encrypt(plainText = text, shiftAmount = shift)
  elif direction =="decoode" or direction =="2":
    text = input("Type your message:\n ->").lower()
    shift = int(input("Type the shift number:\n ->"))
    decrypt(cipherText = text, shiftAmount = shift)
  else:
    print("Sorry, invalid direction choice, please try '1' to encode or '2' to 'decode'.\n")
  
  choice = input("Type 'yes' or '1' if you want to go again. Otherwise type 'no' or '2'.\n ->").lower()
  if choice == "yes" or choice == "1":
    endEncoding = False
  elif choice =="no" or choice == "2":
    endEncoding = True
  else:
    print("Sorry, didn't understand your choice. Termanting program... Happy Encoding!")
    endEncoding = True

    




