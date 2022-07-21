from datetime import datetime, timedelta

clients_list = []
librarians_list = []
books_list = []
borrowed_orders_list = []
total_available_books = []
total_borrowed_orders = []
date_1 = datetime.today()
last_date = date_1 + timedelta(days=10)


class Person:
    def __init__(self, full_name, age, id_number, phone_number):
        self._full_name = full_name
        self._age = age
        self._id_number = id_number
        self._phone_number = phone_number

    def set_full_name(self, full_name):
        self._full_name = full_name

    def get_full_name(self):
        return self._full_name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_id_number(self, id_number):
        self._id_number = id_number

    def get_id_number(self):
        return self._id_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_phone_number(self):
        return self._phone_number


class Client(Person):
    _client_counter = 1

    def __init__(self, full_name, age, id_number, phone_number):
        super().__init__(full_name, age, id_number, phone_number)
        self.id = Client._client_counter
        Client._client_counter += 1


class Librarian(Person):
    _librarian_counter = 1

    def __init__(self, full_name, age, id_number, phone_number, salary=0.0):
        self.id = Librarian._librarian_counter
        super().__init__(full_name, age, id_number, phone_number)
        self.salary = salary
        Librarian._librarian_counter += 1

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


class Book:
    _book_counter = 1

    def __init__(self, book_title, book_description, book_author, book_status):
        self.id = Book._book_counter
        self._book_title = book_title
        self._book_description = book_description
        self._book_author = book_author
        self._book_status = book_status
        Book._book_counter += 1

    def set_book_title(self, book_title):
        self._book_title = book_title

    def get_book_title(self):
        return self._book_title

    def set_book_description(self, book_description):
        self._book_description = book_description

    def get_book_description(self):
        return self._book_description

    def set_book_author(self, book_author):
        self._book_author = book_author

    def get_book_author(self):
        return self._book_author

    def set_book_status(self, book_status):
        self._book_status = book_status

    def get_book_status(self):
        return self._book_status


class BorrowingOrder:
    _borrow_id = 1

    def __init__(self, start_date, end_date, book_name, client_id, borrow_status):
        self.id = BorrowingOrder._borrow_id
        self._start_date = start_date
        self._end_date = end_date
        self._book_name = book_name
        self._client_id = client_id
        self._borrow_status = borrow_status
        BorrowingOrder._borrow_id += 1

    def set_book_name(self, book_name):
        self._book_name = book_name

    def get_book_name(self):
        return self._book_name

    def set_client_id(self, client_id):
        self._client_id = client_id

    def get_client_id(self):
        return self._client_id

    def set_borrow_status(self, borrow_status):
        self._borrow_status = borrow_status

    def get_borrow_status(self):
        return self._borrow_status


books_list.append(
    Book(book_title="Start with Why1", book_description="How Great Leaders Inspire Everyone to Take Action.",
         book_author="Simon Sinek", book_status="active", ))
books_list.append(
    Book(book_title="Start with Why2", book_description="How Great Leaders Inspire Everyone to Take Action.",
         book_author="Simon Sinek", book_status="active", ))
books_list.append(
    Book(book_title="Start with Why3", book_description="How Great Leaders Inspire Everyone to Take Action.",
         book_author="Simon Sinek", book_status="active", ))
books_list.append(
    Book(book_title="Start with Why4", book_description="How Great Leaders Inspire Everyone to Take Action.",
         book_author="Simon Sinek", book_status="active", ))

user_input = input("""
1. Create New Client.
2. Create New Librarian.
3. Borrow Book.
4. Return Book To Librarian.
q. Exit. 
""")
counter = 0
while user_input != "q":
    if counter != 0:
        user_input = input("""
1. Create New Client.
2. Create New Librarian.
3. Borrow Book.
4. Return Book To Librarian.
q. Exit.
""")
    counter += 1
    if user_input == "1":
        client = Client(input("Enter Full Name"), input("Enter Age"), id_number=input("Enter Id Number"),
                        phone_number=input("Enter Phone Number"))
        clients_list.append(client)
        continue
    elif user_input == "2":
        librarian = Librarian(input("Enter Full Name: "), input("Enter Your Age:"), input("Enter Id Number: "),
                              input("Enter Phone Number: "))
        librarians_list.append(librarian)
        continue
    elif user_input == "3":
        for book in books_list:
            print(str(book.id) + ". " + book.get_book_title())
        borrowed_book_id = input("Enter book number you want to borrow: ")
        while int(borrowed_book_id) > len(books_list) or int(borrowed_book_id) < 0:
            borrowed_book_id = input("This id doesn't exists, please try another one:")
        if books_list[int(borrowed_book_id) - 1].get_book_status() != "active":
            borrowed_book_id = input("This book is already borrowed, please try another one:")
        else:
            client_id_number = input("Enter your id: ")
            if len(clients_list) > 0:
                for client in clients_list:
                    if int(client.get_id_number()) == int(client_id_number):
                        borrowed_orders_list.append({
                            "book_id": borrowed_book_id,
                            "client_id": client_id_number,
                            "start_date": date_1,
                            "end_date": last_date
                        })
                        books_list[int(borrowed_book_id) - 1].set_book_status("inactive")
                        print(borrowed_orders_list)
                        print("Book borrowed successfully.")
                    else:
                        input("This client id is not exist, please enter your id correctly: ")
            else:
                print("Please add client before.")
                continue

    elif user_input == "4":
        if len(borrowed_orders_list) <= 0:
            print("There is no borrowed books")
            continue
        else:
            client_id_number = input("Enter your id: ")
            for order in borrowed_orders_list:
                if int(order["client_id"]) == int(client_id_number):
                    print(order["book_id"] + ". " + books_list[int(order["book_id"]) - 1].get_book_title())
                else:
                    print("You don't have any book to return.")
                    continue
            returned_book_id = input("Enter book id you want to return")
            for order in borrowed_orders_list:
                if int(order["book_id"]) == int(returned_book_id):
                    books_list[int(returned_book_id) - 1].set_book_status("active")
                    borrowed_orders_list.remove(order)
                    print("Book returned successfully.")
                    continue
                else:
                    print("You can't return this book.")
                    continue
