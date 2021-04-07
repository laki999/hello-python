import book
import author

# Uses the 3 parameters and calls the classes
first_author = author.Author("John", "doe", "British")
book = book.Book("Python", "1", "john")

book.lend("testUser")