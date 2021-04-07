# the dot means from the same directory
from author import Author

# go look for the class
class Book:
    # def means defining the function
    def __init__(self, title, revision, authors):

        # Define the attributes in the class
        self.title = title
        self.revision = revision
        self.authors = authors

    def lend(self, username):
        print("book {} lent by {}".format(self.title, username))
