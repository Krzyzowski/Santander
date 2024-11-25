osoba = {"imię": "Jan", "wiek": "25", "miasto": "Madryt"}

print(osoba["imię"])  # Wypisuje "Jan"
print(osoba["wiek"])    # Wypisuje "25"
print(osoba["miasto"])  # Wypisuje "Madryt"

print(osoba.keys())    # Wypisuje dict_keys(["imię", "wiek", "miasto"])

print(osoba.values())  # Wypisuje dict_values(["Jan", "25", "Madryt"])

print(osoba.items())   # Wypisuje dict_items([("imię", "Jan"), ("wiek", "25"), ("miasto", "Madryt")])

osoba.update({"zawód": "inżynier"})
print(osoba.items())
print(osoba)