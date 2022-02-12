

class Library:
    def __init__(self, ListofBooks):
        self.books=ListofBooks

    def AvailableBooks(self):
        print('Books present in the Library is: ')
        for book in self.books:
            print(' *' + book)

    def BookBorrow(self, BookName):
        if BookName in self.books:
            print(f'You have been issued {BookName}, Please keep it safe and Return it within 30 days.')
            self.books.remove(BookName)
            return True
        else:
            print('Sorry, This Book either not available or has already been issued!')    
            return False
        
    def BookReturn(self, Bookname):
        self.books.append(Bookname)
        print('Thanks for returning this book, have a nice day ahead.')

class Student():
    def RequestBook(self):
        self.book = input('Enter the name of the book you want to Borrow : ')
        return self.book
    
    def ReturnBook(self):
        self.book = input('Enter the name of the book you want to Return : ')
        return self.book

if __name__=="__main__":
    CentralLibrary=Library(['Java', 'Python', 'The jungle book', 'c++','Data Structure'])
    student=Student()
    while True:
        WelcomeMsg='''\n ==== Welcomes To DRIEMS Library ====
        Please Choose Your Option
        1. List all the Books
        2. Request a Book
        3. Add/Return a Book
        4. Exit the Library
        '''
        print(WelcomeMsg)
        n=input('Enter Your Choice..: ')
        try:
            a = int(n)
            if a==1:
                CentralLibrary.AvailableBooks()
            elif a==2:
                CentralLibrary.BookBorrow(student.RequestBook())
            elif a==3:
                CentralLibrary.BookReturn(student.ReturnBook())
            elif a==4:
                print('Thanks for Choosing Central Library, Have a Great day ahead!.')
                exit()
            else:
                print('Invalid Choice')
        except:
            print('Oops!, Please Enter a valid Number')
            