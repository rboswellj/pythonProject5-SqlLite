# Robert Johnson
# CIT 144
# Project 5

import sqlite3

conn = sqlite3.connect('tickets5.db')
cur = conn.cursor()     # create a cursor from the connection


def main():
    while True:
        printMenu()
        getSelection()

def printMenu():
    print("Menu Options. Select 1, 2, 3, or 4")
    print(" 1. Display All Tickets")
    print(" 2. Add a Ticket")
    print(" 3. Filter by Offender Sex")
    print(" 4. Save and Exit")
    print("----------")
    
def getSelection():
    selector = int(input("Select an Option: "))
    if selector == 1:
        displayAllTickets()
    elif selector == 2:
        addTicket()
    elif selector == 3:
        sexFilter()
    elif selector == 4:
        saveAndExit()
    else:
        print("----------")
        print("Invalid Entry")
        print("Select a valid option")
        selector = input("Select an option 1, 2, 3 or 4")
    print()
    runAgain()

def isNumber(string):
    try:
        int(string)
        return True
    except:
        print('invalid entry. Enter a number')
        return False
    
def addTicket():
    print("----------")
    print("New Ticket Entry")
    actSpeed = input("Enter recorded speed: ")
    actIsNum = isNumber(actSpeed)
    while(actIsNum == False):
        actSpeed = input("Enter recorded speed: ")
        actIsNum = isNumber(actSpeed)
    posted = input("Enter posted speed limit: ")
    postIsNum = isNumber(posted)
    while(postIsNum == False):
        posted = input("Enter posted speed limit: ")
        postIsNum = isNumber(posted)
    age = input("Enter offender's age: ")
    ageIsNum = isNumber(age)
    while(ageIsNum == False):
        age = input("Enter offender's age: ")
        ageIsNum = isNumber(age)
    invalidSex = True
    while invalidSex == True:
        sex = input("Enter offender's sex(m/f): ")
        if sex == 'm' or sex == 'M':
            sex = "Male"
            invalidSex == False
            break
        elif sex == 'f' or sex == 'F':
            sex= "Female"
            invalidSex == False
            break
        else:
            print("Invalid Entry. Enter m or f")
            
    newTicket = Ticket(actSpeed, posted, age, sex)

    sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?)"
    data = (None, int(newTicket.getActualSpeed()), int(newTicket.getPostedSpeed()), int(newTicket.getAge()), newTicket.getSex())
    cur.execute(sql, data)
    conn.commit()
    print("Ticket added")
    print("%-15s %-10s %-6s %-4s " % ('posted-speed', 'MPH Over', 'age', 'sex'))  # headings
    print("%-15s %-10s %-6s %-4s " % (posted, int(actSpeed) - int(posted), age, sex))     


def runAgain():
    print("----------")
    print("Perform another operation(y/n)")
    selector = input("y/n?: ")
    if selector == "y" or selector == "Y":
        return main()
    elif selector == "n" or selector == "N":
        saveAndExit()
    else:
        print("Invalid Entry")
        return runAgain()

def displayAllTickets():
    sql = "SELECT * FROM tickets"    # select all records from travel table
    cur.execute(sql)

    results = cur.fetchall()        # fetchall() returns records as a list of tuples

    if results:
        printData(results)         # if records were found, print them
    else:
        print('No data found')    
    print() 
    runAgain()

def sexFilter():
    print("-----------")
    print("View All tickets by Sex of Offender")
    selector = input("Enter m for male or F for female: ")
    if (selector == "m" or selector == "M"):
        gender = ("Male", )
    elif (selector == "f" or "F"):
        gender = ("Female", )
    else:
        print("Invalid entry")
        print("Select m for Male or f for female")
        return sexFilter()    
    sql = "SELECT * FROM tickets WHERE violator_sex = ?"    # select all records from travel table
    cur.execute(sql, gender)
    results = cur.fetchall()        # fetchall() returns records as a list of tuples

    if results:
        printData(results)         # if records were found, print them
    else:
        print('No data found')
     
    print()

def saveAndExit():
    print("Save and Exit?")
    selection = input("(y/n): ")
    if selection == 'y' or selection == 'Y':
        exit()
    elif selection == 'n' or selection == 'N':
        main()

def printData(data):
    print(" %-8s %-15s %-10s %-6s %-4s " % ('tid', 'posted-speed', 'MPH Over', 'age', 'sex'))  # headings

    for row in data:
        mphOver = row[1] - row[2]
        print(" %-8s %-15s %-10s %-6s %-4s " % (row[0], row[2], mphOver, row[3], row[4]))     
     
    print()

class Ticket():
    def __init__(self, actualSpeed, postedSpeed, age, sex):
        self._actual_speed = actualSpeed
        self._posted_speed = postedSpeed
        self._age = age
        self._sex = sex

    def getActualSpeed(self):
        return self._actual_speed
    
    def getPostedSpeed(self):
        return self._posted_speed

    def getAge(self):
        return self._age

    def getSex(self):
        return self._sex

    def getMphOver(self):
        return self._actual_speed - self._posted_speed

main()