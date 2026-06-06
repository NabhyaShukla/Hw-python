books = ["Wallah The Great", "Al Habibi", "Harry My Bri'ish Po'ah", "GTA: The Frank", "HP: Cursed Omnibook X7", "WTF: Whats That Fish?"]
print(len(books)) # len() = length of the list
print(books[0]) # indexing starts at 0, so the first element is at index 0 and it prints the first element of the list
print(books[-1]) # negative indexing starts at -1, so the last element is at index -1 and it prints the last element of the list
print(books[:3]) # slicing the list, it prints the first 3 elements of the list (index 0, 1, and 2)
print("*" * 129)

books.append("The fraudulent gatsby") # appending a new element to the end of the list
books.remove("HP: Cursed Omnibook X7") # removing an element from the list
books.sort() # sorting the list in alphabetical order
books.reverse() # reversing the order of the list

librarian = {
    "name" : "Mr. Woah",
    "age" : 92,
    "experience" : "70 years",
}

print(librarian["name"]) # accessing the value of the key "name" in the dictionary
librarian["age"] = 29 # updating the value of the key "age" in the dictionary
librarian["experience"] = "07 years"
librarian["favorite_book"] = "Harry My Bri'ish Po'ah"
librarian["email"] = "mr.woahoo@yahoo.com" 
librarian["working-hours-per-day"] = "25 Hours/day"

book_ids = [121, 122, 212, 221, 313, 331]
book_dictionary = dict(zip(books, book_ids)) # creating a dictionary by zipping the list of books and the list of book ids together
print("*" * 129)


print("LIBRARY CATALOG (Chaman Nagar, Maudiyan, U.P., India, Earth, Solar System, Milky Way, Universe)")
print("=" * 129)
print("Librarian Details : ", librarian)
print("Books Available : ", books)
print("Book IDs Directory: ", book_dictionary)
print("=" * 129)
print("THANKS FOR VISITING OUR LIBRARY, HOPE TO SEE YOU AGAIN SOON!")