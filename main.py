import sqlite3

conn = sqlite3.connect('tickets5.db')  # create cars.sqlite, establish connection to db
cur = conn.cursor()     # create a cursor from the connection


def main():
    displayAllTickets()


def displayAllTickets():
    sql = "SELECT * FROM tickets"    # select all records from travel table
    cur.execute(sql)

    results = cur.fetchall()        # fetchall() returns records as a list of tuples

    if results:
        printStuff(results)         # if records were found, print them
    else:
        print('No data found')
     
    print()


def printStuff(data):    # helper function, just prints whatever was selected
    print(" %-8s %-15s %-10s %-6s %-4s " % ('tid', 'actual-speed', 'posted-speed', 'age', 'sex'))  # headings

    for row in data:
        print(" %-8s %-15s %-12s %-6s %-4s " % (row[0], row[1], row[2], row[3], row[4]))     
        # print(row)
     
    print()

main()