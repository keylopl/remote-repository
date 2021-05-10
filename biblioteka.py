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
#my_cursor.execute("CREATE DATABASE biblioteka")

# sprawdzenie czy stworzylismy biblioteke
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#	print(db)

# tworzenie tabeli
my_cursor.execute("CREATE TABLE IF NOT EXISTS ksiazki (tytul VARCHAR(255), \
	imie_autora VARCHAR(255), \
	nazwisko_autora VARCHAR(255), \
	rok_wydania INT(10), \
	ksiazki_id INT AUTO_INCREMENT PRIMARY KEY)")

# wyswietlenie tabeli
#my_cursor.execute("SELECT * FROM ksiazki")
#print(my_cursor.description)

#for thing in my_cursor.description:
#	print(thing)

root.mainloop()