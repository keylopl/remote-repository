from tkinter import *
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.geometry("350x600")
root.title("Biblioteka")

# laczenie do bazy danych
mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "admin",
		database = "biblioteka",
	)

# sprawdzenie czy polaczylismy sie z baza danych
# print(mydb)

# tworzenie cursora
my_cursor = mydb.cursor()

# tworzenie database
my_cursor.execute("CREATE DATABASE biblioteka")

# sprawdzenie czy stworzylismy biblioteke
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)


root.mainloop()