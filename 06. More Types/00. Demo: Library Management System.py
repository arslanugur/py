# Dictionary Functions
# A library management program has a dictionary of books with their corresponding genres.

# Take a book name as input and output the genre.
# If the book is not present in the dictionary, output "Not found".


# Input: Watchmen         Output: Comics
# Input: Life of Pi       Output: Adventure Fiction


# Code:
books = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

if book in books:
    print(books[book])
else:
    print("Not found")
#



