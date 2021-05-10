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
    


# Szukanie po tytule
def search_book():
	search_books = Tk()
	search_books.title("Szukaj książki")
	search_books.geometry("1100x800")
	def seach_now():
		searched = search_box.get()
		sql = "SELECT ksiazki_id, tytul, imie_autora, nazwisko_autora, rok_wydania FROM ksiazki WHERE tytul = %s"
		name = (searched, )
		result = my_cursor.execute(sql, name)
		result = my_cursor.fetchall()

		if not result:
			result = "Nie znaleziono tytułu..."
			searched_label = Label(search_books, text=result)
			searched_label.grid(row=2, column=0)

		else:
			for index, x in enumerate(result):
				num = 0
				index += 2
				for y in x:
					searched_label = Label(search_books, text=y)
					searched_label.grid(row=index, column=num+1)
					num +=1


    # Entry box do szukania ksiazki
	search_box = Entry(search_books)
	search_box.grid(row=0, column=1, padx=10, pady=10)
    # Entry box Label do szukania ksiazki
	search_box_label = Label(search_books, text="Szukaj książki po tytule: ")
	search_box_label.grid(row=0, column=0, padx=10, pady=10)
	# Entry box search Button do szukania ksiazki
	search_button = Button(search_books, text="Szukaj książki", command=seach_now)
	search_button.grid(row=1, column=0, padx=10)

# Szukanie po autorze
def search_book2():
	search_books2 = Tk()
	search_books2.title("Szukaj książki")
	search_books2.geometry("1100x800")
	def seach2_now():
		searched2 = search_box2.get()
		sql = "SELECT ksiazki_id, tytul, imie_autora, nazwisko_autora, rok_wydania FROM ksiazki WHERE concat(imie_autora, ' ', nazwisko_autora) = %s"
		name = (searched2, )
		result = my_cursor.execute(sql, name)
		result = my_cursor.fetchall()

		if not result:
			result = "Nie znaleziono autora..."
			searched2_label = Label(search_books2, text=result)
			searched2_label.grid(row=2, column=0)
		else:
			for index, x in enumerate(result):
				num = 0
				index += 2
				for y in x:
					searched2_label = Label(search_books2, text=y)
					searched2_label.grid(row=index, column=num+1)
					num +=1			



    # Entry box do szukania ksiazki
	search_box2 = Entry(search_books2)
	search_box2.grid(row=0, column=1, padx=10, pady=10)
    # Entry box Label do szukania ksiazki
	search_box2_label = Label(search_books2, text="Szukaj książki po autorze: ")
	search_box2_label.grid(row=0, column=0, padx=10, pady=10)
	# Entry box search Button do szukania ksiazki
	search2_button = Button(search_books2, text="Szukaj książki", command=seach2_now)
	search2_button.grid(row=1, column=0, padx=10)




# lista ksiazek
def list_books():
	list_book_query = Tk()
	list_book_query.title("Lista książek")
	list_book_query.geometry("800x600")
	# zapytanie do bazy
	my_cursor.execute("SELECT * FROM ksiazki")
	result = my_cursor.fetchall()

	for index, x in enumerate(result):
		num = 0
		for y in x:
			lookup_label = Label(list_book_query, text=y)
			lookup_label.grid(row=index, column=num)
			num +=1



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

# guzik do listy ksiazek
list_books_button = Button(root, text="Wyświetl liste książek", command=list_books)
list_books_button.grid(row=16, column=0, sticky=W, padx=10)	

# Szukaj po tytule
search_books_button = Button(root, text="Szukaj po tytule", command=search_book)
search_books_button.grid(row=15, column=1, sticky=W, padx=10)

# Szukaj po autorze
search_books2_button = Button(root, text="Szukaj po autorze", command=search_book2)
search_books2_button.grid(row=15, column=0, sticky=W, padx=10, pady=10)





root.mainloop()