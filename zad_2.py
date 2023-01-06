# Zad 2
# a
def wyswietl_imiona(imiona):
    for imie in imiona:
        print(imie)


imiona = ['Anna', 'Tomasz', 'Jan', 'Katarzyna', 'Marcin']
wyswietl_imiona(imiona)


# b (wykorzystując pętle for)
def pomnoz_przez_dwa(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_dwa(liczby)
print(wynik)


# b (wykorzystując listę składaną)
def multiply_by_two(numbers):
    return [x * 2 for x in numbers]


print(multiply_by_two([1, 2, 3, 4, 5]))


# c
def print_even(numbers):
    for x in numbers:
        if x % 2 == 0:
            print(x)


print_even(range(10))


# d
def print_even(numbers):
    for i, x in enumerate(numbers):
        if i % 2 == 0:
            print(x)


print_even(range(10))
