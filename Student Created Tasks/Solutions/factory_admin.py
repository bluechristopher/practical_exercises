# Task 1
import sqlite3


conn = sqlite3.connect("FACTORY.db")
cursor = conn.cursor()

# create Good table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Good(
        GoodID INTEGER PRIMARY KEY,
        GoodName TEXT NOT NULL,
        Category TEXT NOT NULL);
''')

# create Machine table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Machine(
        MachineID INTEGER PRIMARY KEY,
        MachineName TEXT NOT NULL,
        Status TEXT NOT NULL);
''')

# create Production table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Production(
        ProductionID INTEGER PRIMARY KEY,
        GoodID INTEGER NOT NULL,
        MachineID INTEGER NOT NULL,
        Quantity INTEGER NOT NULL,
        Quality TEXT NOT NULL,
        DateProduced TEXT NOT NULL,
        FOREIGN KEY (GoodID) REFERENCES Good(GoodID),
        FOREIGN KEY (MachineID) REFERENCES Machine(MachineID));
''')

conn.commit()
conn.close()

# Task 2
import csv


# goods table
# file closes after with block
with open("GOODS.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        cursor.execute('''
            INSERT INTO Good (GoodID, GoodName, Category)
            VALUES (?, ?, ?);
        ''', row)
