from operator import truediv
from urllib import request


class Library:
    def __init__(self,Listofbooks):
        self.books=Listofbooks

    def Availablebooks(self):
        print('The Books present in the Library is :')
        for book in self.books:
            print(' *' + book)
            
    def BorrowBook(self,book):
        if book in self.books:
            print(f'You have been issued {book}, Please keep it safe and Return under 30 days')
            self.books.remove(book)
            return True
        else:
            print('Oops!,You issued book is not available! and try another days')
            return False
    
    def Returnbook(self,book):
        self.books.append(book)
        print('Thanks for returning the book, I hope you enjoyed and have a great day')
    
class Student:
    def Requestbook(self):
        self.books=input('Enter a book name you want to be borrow : ')
        return self.books
    
    def Returnbook(self):
        self.books=input('Enetr a book name to return :')
        return self.books

if __name__=="__main__":
    CentralLibrary= Library(['java', 'Python', 'c', 'jungle book','data structure'])
    student=Student()
    while True:
        welcomeMsg='''\n ==== Welcome To Central Library ====
        Please Choose an Options: 
        1. List of Books
        2. Borrow the Book
        3. Return the book
        4. exit
        '''
        print(welcomeMsg)
        try:
            p = int(input('Enter your choice: '))
            if p == 1:
                CentralLibrary.Availablebooks()
            elif p == 2:
                CentralLibrary.BorrowBook(student.Requestbook())
            elif p == 3:
                CentralLibrary.Returnbook(student.Returnbook())
            elif p == 4:
                print('Thank you for coming our Library.')
                break
            else:
                print('Invalid Choice!')
        except:
            print('Input a valid Number for Choice Options')
                
    



