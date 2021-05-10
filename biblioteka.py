from tkinter import *
import mysql.connector


root = Tk()
root.geometry("350x600")
root.title("Biblioteka")

# laczenie do bazy danych
mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "admin",
	)

sprawdzenie czy polaczylismy sie z baza danych
print(mydb)


root.mainloop()