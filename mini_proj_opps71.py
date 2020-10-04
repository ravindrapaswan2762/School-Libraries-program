

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if(k==1):
        c = int(input("enter 1 for ADD and 2 for RETURN books : "))
        if(c==1):
            value = input("Type here for add books\n")
            with open("harry_add.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully added")
        if(c==2):
            value = input("Type here for return books\n")
            with open("harry_return.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully returned")



    elif(k==2):
        c = int(input("enter 1 for ADD and 2 for RETURN books : "))
        if (c == 1):
            value = input("type here for add books\n")
            with open("rohan_add.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully added")

        if (c == 2):
            value = input("type here for return books\n")
            with open("rohan_return.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully returned")


    elif(k==3):
        c = int(input("enter 1 for ADD and 2 for DISPLAY books : "))
        if (c == 1):
            value = input("type here for add books\n")
            with open("ravindra_add.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully added")

        elif(c == 2):
            value = input("type here for return books\n")
            with open("ravindra_return.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully returned")

    else:
            print("please enter valid no. 1(harry), 2(rohan), 3(ravindra) : ")


def retrieve(k):
    if(k==1):
        c = int(input("enter 1 for ADDED and 2 for RETURNED display books for HARRY : "))
        if(c==1):
            with open("harry_add.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif(c==2):
            with open("harry_return.txt")as op:
                for i in op:
                    print(i, end=" ")

    elif(k==2):
        c = int(input("enter 1 for ADDED and 2 for RETURNED display books for ROHAN : "))
        if (c == 1):
            with open("rohan_add.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("rohan_return.txt")as op:
                for i in op:
                    print(i, end=" ")


    elif(k==3):
        c = int(input("enter 1 for ADDED and 2 for RETURNED display books for RAVINDRA  : "))
        if (c == 1):
            with open("ravindra_add.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("ravindra_return.txt")as op:
                for i in op:
                    print(i, end=" ")


    else:
        print("please enter valid input (harry, rohan, ravindra) : ")


a = int(input("press 1 for ADD/RETURN  the books and 2 for DISPLAY-BOOKS : "))
if(a==1):
    b = int(input("press 1 for HARRY, 2 for ROHAN and 3 for RAVINDRA : "))
    take(b)

else:
    b = int(input("press 1 for HARRY, 2 for ROHAN and 3 for RAVINDRA : "))
    retrieve(b)
########################################################################################################################

##########################################################################################################

# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
"""import re


class Library:
    # name = library name, list = library list
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)


    def lendBook(self, user, book):
        #if book not in self.lendDict.keys():
              ### OR  ##
        if book in self.booksList and book not in self.lendDict:
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")

        else:
            print(f"Book is already being used by {self.lendDict[book]}")


    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")

    while(True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
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
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue"""
###################################################################################################
####################################################################################################
















