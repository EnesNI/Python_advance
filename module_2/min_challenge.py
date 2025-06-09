# Requirements:
# ● Create the dictionary: Begin with creating a dictionary where the keys are tuples of book titles and authors, and the values are genres.
# ● Add a New Book: Add a new entry to the dictionary with a tuple containing the title and author of the new book, and set its genre.
# ● Retrieve and Print Book Information: Retrieve and print the genre of a book given its title and author.


library = {
    ("1984", "George Orwell"): "Dystopian",
    ("To Kill a Mockingbird", "Harper Lee"): "Fiction",
    ("A Brief History of Time", "Stephen Hawking"): "Science",
}


library[("The Great Gatsby", "F. Scott Fitzgerald")] = "Classic"


print(library[("1984", "George Orwell")])
