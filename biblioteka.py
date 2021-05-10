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

# czyszczenie pol tekstowych
def clear_fields():
	tytul_box.delete(0, END)
	imie_autora_box.delete(0, END)
	nazwisko_autora_box.delete(0, END)
	rok_wydania_box.delete(0, END)


# dodanie ksiazki do bazy
def add_book():
	sql_command = "INSERT INTO ksiazki (tytul, imie_autora, nazwisko_autora, rok_wydania) VALUES (%s, %s, %s, %s)"
	values = (tytul_box.get(), imie_autora_box.get(), nazwisko_autora_box.get(), rok_wydania_box.get())
	my_cursor.execute(sql_command, values)

	# commit do bazy
	mydb.commit()
	# czyszczenie pol
	clear_fields()
    




# tworzenie etykiety
title_label = Label(root, text="Baza ksiazkowa", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#glowny formularz do dodawania danych ksiazek
tytul_label = Label(root, text="Tytuł").grid(row=1, column=0, sticky=W, padx=10)
imie_autora_label = Label(root, text="Imie autora").grid(row=2, column=0, sticky=W, padx=10)
nazwisko_autora_label = Label(root, text="Nazwisko autora").grid(row=3, column=0, sticky=W, padx=10)
rok_wydania_label = Label(root, text="Rok wydania").grid(row=4, column=0, sticky=W, padx=10)

# tworzenie boxow do wpisania danych
tytul_box = Entry(root)
tytul_box.grid(row=1, column=1)

imie_autora_box = Entry(root)
imie_autora_box.grid(row=2, column=1, pady=5)

nazwisko_autora_box = Entry(root)
nazwisko_autora_box.grid(row=3, column=1, pady=5)

rok_wydania_box = Entry(root)
rok_wydania_box.grid(row=4, column=1, pady=5)

# guziki do dodawania ksiazek
add_book_button = Button(root, text="Dodaj książke do bazy", command=add_book)
add_book_button.grid(row=14, column=0, padx=10, pady=10)
clear_fields_button = Button(root, text="Wyczyść pola", command=clear_fields)
clear_fields_button.grid(row=14, column=1)







root.mainloop()