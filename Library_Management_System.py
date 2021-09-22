from difflib import get_close_matches


class Library:
    borrowed_book_list = []

    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_available_books(self):
        print()
        print('Available Books : ')
        books_printing_list = sorted(self.available_books)
        for book in books_printing_list:
            print(book)

    def lend_book(self, requested_book):
        requested_book = requested_book.title()
        if requested_book in self.available_books:
            print('You have now borrowed the book')
            temp = requested_book
            self.available_books.remove(requested_book)
            self.borrowed_book_list.append(temp)
        else:
            book_name = get_close_matches(requested_book, self.available_books)
            y_or_n = input(
                'Do you mean {} ? Enter yes or no : '.format(book_name[0]))
            if y_or_n.lower() == 'yes':
                print('You have now borrowed the book')
                temp = book_name[0]
                self.available_books.remove(book_name[0])
                self.borrowed_book_list.append(temp)
            elif y_or_n.lower() == 'no':
                print('No such book available. Please check the book-name')
            else:
                print('Please enter either yes or no')

    def add_book(self, returned_book):
        if returned_book in self.borrowed_book_list:
            self.available_books.append(returned_book.title())
            print('You have returned the book. Thank You!')
        # else:
        #     book_name_2 = get_close_matches(
        #         returned_book, self.borrowed_book_list)
        #     this_book = book_name_2[0]
        #     y_or_n = input(
        #         'Do you mean {} ? Enter yes or no : '.format(this_book))

            # if y_or_n.lower() == 'yes':
            #     try:
            #         self.available_books.append(this_book.title())
            #         print('You have returned the book. Thank You!')
            #     except IndexError:
            #         print('You have not borrowed this book!')
            # elif y_or_n.lower() == 'no':
            #     print('No such book lent. Please check the book-name')
            # else:
            #     print('Please enter either yes or no')


class Customer:
    def request_book(self):
        print('Enter the name of the book you would like to borrow : ')
        self.book = input().title()
        return self.book

    def return_book(self):
        print('Enter the name of book which you are returning : ')
        self.book = input().title()
        if self.book != '':
            return self.book
        else:
            print('Please enter the name of your book')


library = Library(['Wings Of Fire', 'Atomic Habits', 'The 5 Am Club'])
customer = Customer()
while True:
    print()
    print('Enter 1 to display the available books')
    print('Enter 2 to request a book')
    print('Enter 3 to return a book')
    print('Enter 4 to exit')
    user_choice = int(input('Enter your choice : '))
    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        req_book = customer.request_book()
        library.lend_book(req_book)
    elif user_choice == 3:
        ret_book = customer.return_book()
        library.add_book(ret_book)
    elif user_choice == 4:
        print('Thank You!')
        quit()
    else:
        user_choice = int(input('Enter a number from the ones shown above : '))
