class Library:
    def __init__(self,l_book,l_name):
        self.listofbooks=l_book
        self.library_name=l_name
        self.dic = {}

    def display_books(self):
        print (f"THE BOOKS AVAILABLE IN LIBRARY {self.library_name} ARE:\n ")
        for a in self.listofbooks:
            print(a)

    def lend_book(self,book_name,lend_to):
        if book_name not in self.dic.keys():
            self.dic.update({book_name:lend_to})
        else:
           print(f"THE BOOK HAS BEEN ALREADY BEEN LEND TO :{self.dic[book_name]}")

    def add_book(self,book_name):
        self.listofbooks.append(book_name)
        print(f"THE BOOK HAS BEEN ADDED")

    def return_book(self,book_name):
            self.dic.pop(book_name)

if __name__ == '__main__':
    harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "ABHINAV'S LIBRARY")

    while(True):
        print(f"Welcome to the {harry.library_name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.display_books()
        elif user_choice == 2:
            book = input("ENTER THE NAME OF THE BOOK YOU WANT TO LEND:")
            user = input("ENTER YOUR NAME:")
            harry.lend_book(book,user)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.add_book(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.return_book(book)
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue


