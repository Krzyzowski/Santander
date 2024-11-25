
def powitanie():
    print("Witaj, Świecie!")


powitanie()  # Wypisuje "Witaj, Świecie!"

def powitanie(imię):
    print(f"Witaj, {imię}!")

powitanie("Jan")  # Wypisuje "Witaj, Jan!"
powitanie("Maria")  # Wypisuje "Witaj, Maria!"


print( )
print("return")
def dodawanie(a, b):
    return a + b


wynik = dodawanie(3, 4)
print(wynik)  # Wypisuje 7

print( )
print("Funkcje anonimowe (lambda)")
kwadrat = lambda x: x ** 2
print(kwadrat(5))  # Wypisuje 25

print( )
print("Zasięg zmiennych (lokalny vs. globalny)")

def funkcja():
    zmienna_lokalna = 10
    print(zmienna_lokalna)  # Dostępna wewnątrz funkcji

zmienna_globalna = 20

def funkcja2():
    print(zmienna_globalna)  # Dostępna z dowolnego miejsca


funkcja()  # Wypisuje 10
funkcja2()  # Wypisuje 20
print(zmienna_globalna)  # Wypisuje 20
#print(zmienna_lokalna)  # Generuje błąd, zmienna nie jest zdefiniowana w tym zasięgu.

def zmienna_dodawanie(*liczby):
    total = 0
    for cyfra in liczby:
        total += cyfra
    return total

