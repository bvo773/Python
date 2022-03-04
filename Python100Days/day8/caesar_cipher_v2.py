'''
Caesar Cipher is s way of encoding and decoding text back in the Roman Emperor days. 
Julius Cesar would shift each letter of the alphabet by a certain
predetermined amounts.

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

#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

author: vbspaceduck 
replit: https://replit.com/@vbspaceduck/Caesar-Cipher#main.py
comment: please feel free to fork and add more features or your version of it
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Combine the encrypt and decrypt functions into a single function called caesar(). 
def caesar(startText, shiftAmount, cipherDirection):
  endText = ""
  for char in startText:
    if char not in alphabet:
      endText += char
    else:
      position = alphabet.index(char)
      if cipherDirection == "encode" or cipherDirection == "1":
        newPosition = (position + shiftAmount) % len(alphabet)
      elif cipherDirection == "decode" or cipherDirection=="2":
        newPosition = (position - shiftAmount) % len(alphabet)
      endText += alphabet[newPosition]

  if cipherDirection == "encode" or cipherDirection == "1":
    print(f"Here is your ENCRYPTED Text:\n ->{endText}")
  elif cipherDirection == "decode" or cipherDirection == "2":
    print(f"Here is the DECRYPTED Text:\n ->{endText}")
  else:
    print("Sorry, invalid direction choice, please try '1' to encode or '2' to 'decode'.\n")


# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
from caesar_logo_ascii import logo
print(logo)
shouldCountinue = True
while shouldCountinue:
  direction = input("Type 'encode' or '1' to encrypt, type 'decode' or '2' to decrypt:\n ->").lower()
  text = input("Type your message:\n ->").lower()
  shift = int(input("Type the shift number:\n ->"))

  # Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.   
  caesar(startText=text, shiftAmount=shift, cipherDirection=direction)
  
  choice = input("Type 'yes' or '1' if you want to go again. Otherwise type 'no' or '2'.\n ->").lower()
  if choice == "yes" or choice == "1":
    shouldCountinue = True
  elif choice =="no" or choice == "2":
    shouldCountinue = False
    print("Good bye... Thanks for using the Caesar Cipher Terminal.")
  else:
    print("Sorry, didn't understand your choice. Termanting program... Happy Encoding!")
    shouldCountinue = False





