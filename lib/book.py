#!/usr/bin/env python3

class Book:
    def __init__(self, title_param, page_count_param, current_page_param = 69):
        self.title = title_param
        self.page_count = page_count_param
        self.current_page = current_page_param
       
    # def get_book_title(self):
    #     print(self.title)
    #     return self.title
    @property #page count getter
    def page_count(self):
        return self._page_count
    
    @page_count.setter #page count setter
    def page_count(self, page_count_param):
        if isinstance(page_count_param, int):
             self._page_count = page_count_param
        else: 
            print("page_count must be an integer")       
    
    def turn_page(self):
        self.current_page += 1
        print("Flipping the page...wow, you read fast!")  
          
    def __repr__(self):
        return f"<Book {self.title} {self.page_count}>"



# new_book = Book('And Then There Were None', 272)
# new_book.page_count = 60
# print(new_book)

    
# print(new_book)

 # def turn_page(self):
    #     reading_page = self.current_page
    #     if reading_page > self.current_page:
    #         print("Flipping the page...wow, you read fast!")    

# current_page = 100

# def turn_page(num)
#     if current_page += :

# def Book(new_book):
#     print(new_book.title)
#     print(new_book.get_book_page)
#     return 

