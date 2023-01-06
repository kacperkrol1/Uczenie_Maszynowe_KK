class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"{self.city}|{self.street}|{self.zip_code}|{self.open_hours}|{self.phone}|"


class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.hire_date},{self.birth_date}," \
               f"{self.city},{self.street},{self.zip_code},{self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Data publikacji +{self.publication_date} Autor {self.author_name} {self.author_surname} " \
               f"Ilosc stron {self.number_of_pages} "


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Zamówienie obsługiwane przez {self.employee} Zamówione przez {self.student} " \
               f"Zawartosc {str(str([ksiazka]) for ksiazka in self.books)} data {self.order_date}"


l1 = Library('Warszawa', 'Mikolaja Kopernika', '38-290', '8-20', 322421567)
l2 = Library('Buenos Aires', 'Gruszki', '21-410', '12-18', 533424883)

e1 = Employee('Juan', 'Espanol', '18.07.1960', '18.05.1940', 'Katowice', 'Wadowicka', '18-190', 554344675)
e2 = Employee('Michal', 'Banan', '21.02.1970', '13.06.1940', 'Gorzow', 'Michalska', '30-300', 123456789)
e3 = Employee('John', 'Gorlicki', '23.08.2000', '18.05.1980', 'Michalice', 'Michalicka', '10-120', 332244189)

b1 = Book(l1, '07.07.1990', 'Michał', 'Gdanski', '120')
b2 = Book(l1, '02.03.2001', 'Henryk', 'Walski', '310')
b3 = Book(l2, '04.05.2002', 'Paweł', 'Szklarski', '400')
b4 = Book(l2, '04.02.2003', 'Patryk', 'Wolski', '800')
b5 = Book(l2, '08.09.2001', 'Henryk', 'Malobadzki', '112')

o1 = Order(e1, 'Andrzej Hubert', [b1, b2, b3], '07.07.2017')
o2 = Order(e2, 'Julia Juliowska', [b2], '07.07.2016')

print(o1)
print(o2)