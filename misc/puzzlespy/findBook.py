# Check if a book exists in your collection
collectionOfBooks = ["The Hunger Games", "Bible", "Java for Dummies"]
bookToSearch = input("Enter a book to search for: ")

while not(bookToSearch.isalpha()):
    bookToSearch = input("Please enter a valid book type to search ")
    if (bookToSearch.isalpha()):
        print(bookToSearch)
        break

for book in collectionOfBooks:
    if(book == bookToSearch):
        print("Yes! I do have that book in my collection! :)")
        break
else:
    print("No, I don't have that book in my collection... :(")
