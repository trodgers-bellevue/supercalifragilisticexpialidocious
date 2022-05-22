name = ""
address = ""
phone_number = ""
filename = 'address_book.txt'

while True:
    go_on = input("Would you like to enter a new address (1) amend an address (2) or quit (3)? ")
    if go_on == '1':
        print("Welcome to the Rodgers' address book")
        print("Let's start with some basic information.")
        name = input("What is your name?         :")
        address = input("and your address?          :")
        phone_number = input("phone number?              :")
        
        #append to a text file
        with open('address_book.txt', 'w') as fileobject:
            fileobject.write(name )
            fileobject.write("\n")
            fileobject.write(address )
            fileobject.write("\n")
            fileobject.write(phone_number )
            fileobject.write("\n")

       
    if go_on == '2':
        name = input("What is your name?         :")
        address = input("and your address?          :")
        phone_number = input("phone number?              :")
        #append to a text file
        with open('address_book.txt', 'a') as fileobject:
            fileobject.write(name )
            fileobject.write("\n")
            fileobject.write(address )
            fileobject.write("\n")
            fileobject.write(phone_number )
            fileobject.write("\n")
   
    if go_on == '3':
        #quit and print the text file
        print("Thank you for using this dictionary. ")
        print("This is what we have so far:")
        file=open('address_book.txt' , 'r')
        f = file.readlines()
        print(f)
        break