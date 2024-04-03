class Book:
    
    def __init__ (self, name, author, genre, pages, year, availability, library=1):
        
            self.name = name
            self.author = author
            self.genre = genre
            self.pages = pages
            self.year = year
            self.library = library
            if self.name in self.library.books_lst:   # status             
                self.availability = availability
                print(f"We have {self.name} now")

            else:
                 print(f"We do not have {self.name}")
    
    def show_all_book_info (self):
        print(f"Name: {self.name}\nAuthor: {self.author} \nGenre: {self.genre} \nPages: {self.pages} \nYear: {self.year}")




class Library: 
     
    def __init__(self, readers_list, book_list):
          self.readers_list = readers_list
          self.book_list = book_list
          self.books_lst = ["Christmas Carol", "Crime", "Titanic", "Zodiac"] # main book list

    def add_book(self, name):
         if isinstance (name, str):
              self.name = name
              self.books_lst.append(self.name)
              print(f"The book {name} is added")

    def remove_book(self, name):
         if name in self.books_lst:     
               self.books_lst.remove(name)
               print(f"The book {name} is deleted")
         else:
              print("We do not have this book in our library")

    def give_info(self, bk_name):
         if bk_name in self.books_lst:
              print('We have this book')
         else:
              print("We do not have this book yet")
              
class Reader:
    
    readers = [] # users list

    def __init__ (self, name, surname, age, number, library):
            if isinstance (name, str) and isinstance(surname, str):
               self.name = name
               self.surname = surname
               print(self.name, self.surname)
            if isinstance(age, int) and isinstance(number, int):
                self.age = age
                self.number = number
                print(f"Age: {self.age}\nNumber: {self.number}")
            self.books = []
            self.library = library

    def register_user(self, name_surname):
            if isinstance (name_surname, str):
                self.name_surname = name_surname
                self.readers.append(self.name_surname)
                print(f"New user {self.name_surname} is registered")
            else:
                 print("Please enter a valid name")

    def give_book(self, us_name, bk_name):
         if us_name in self.readers:
              if bk_name in self.books:
                   print(f"{us_name} alredy has it")
              elif bk_name in self.library.books_lst:  # acess to list from the another class
                    self.books.append(bk_name)
                    print(f"{us_name}, '{bk_name}' is added to your purchase") 
              else:
                print(f"Sorry, the book '{bk_name}' is not available in the library")
         else:
              print("Please register first")
              

              
    def check(self):
        print(self.readers)        


library1 = Library(True, True)
library1.add_book("Christmas Carol")
library1.give_info("Christmas Carol")
print(library1.books_lst)


reader1 = Reader("Andrii", "Stakhov", 18, 1, library1)
reader1.register_user("Semen Stakhov")
reader1.register_user("Andrii")
reader1.check()
reader1.give_book("Andrii", "Christmas")


book1 = Book("kjnksv", "A. Stakhov", "Detective", 122, 1999, 1, library1)
book1.show_all_book_info()