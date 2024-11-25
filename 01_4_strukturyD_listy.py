owoce = ["jabłko", "banan", "pomarańcza"]

print(owoce[0])  # Wypisuje "jabłko"
print(owoce[1])  # Wypisuje "banan"
print(owoce[2])  # Wypisuje "pomarańcza"

print(owoce[-1])  # Wypisuje "pomarańcza"
print(owoce[-2])  # Wypisuje "banan"
print(owoce[-3])  # Wypisuje "jabłko"

print( )
print("append")
owoce.append("gruszka")
print(owoce)  # Wypisuje ["jabłko", "banan", "pomarańcza", "gruszka"]

print( )
print("insert")
owoce.insert(1, "winogrona")
print(owoce)  # Wypisuje ["jabłko", "winogrona", "banan", "pomarańcza", "gruszka"]

print( )
print("insert")
owoce.remove("banan")
print(owoce)  # Wypisuje ["jabłko", "winogrona", "pomarańcza", "gruszka"]


print( )
print("pop")
usunięty_owoc = owoce.pop(2)
print(owoce)  # Wypisuje ["jabłko", "winogrona", "gruszka"]
print(usunięty_owoc)  # Wypisuje "pomarańcza"

print( )
print("sort")
owoce.sort()
print(owoce)  # Wypisuje ["jabłko", "gruszka", "winogrona"]
owoce.sort(reverse=True)
print(owoce)
owoce.sort(reverse=False)
print(owoce)

print( )
print("reverse")
owoce.reverse()
print(owoce)  # Wypisuje ["winogrona", "gruszka", "jabłko"]

print( )
print("listy składane")
liczby = [1, 2, 3, 4, 5]
kwadraty = [x ** 2 for x in liczby if x % 2 == 0]
print(kwadraty)  # Wypisuje [4, 16]
