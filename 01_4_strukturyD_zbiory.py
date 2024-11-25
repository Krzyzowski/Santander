
zbiór1 = {1, 2, 3}
zbiór2 = {3, 4, 5}


union = zbiór1 | zbiór2
print(union)  # Wypisuje {1, 2, 3, 4, 5}

intersection = zbiór1 & zbiór2
print(intersection)  # Wypisuje {3}

difference = zbiór1 - zbiór2
print(difference)  # Wypisuje {1, 2}

symmetric_difference = zbiór1 ^ zbiór2
print(symmetric_difference)  # Wypisuje {1, 2, 4, 5}

owoce = {"jabłko", "banan", "pomarańcza"}


owoce.add("gruszka")
print(owoce)  # Wypisuje {"jabłko", "banan", "pomarańcza", "gruszka"}

owoce.remove("banan")
print(owoce)  # Wypisuje {"jabłko", "pomarańcza", "gruszka"}

owoce.discard("winogrona")
print(owoce)  # Wypisuje {"jabłko", "pomarańcza", "gruszka"}

owoce.clear()
print(owoce)  # Wypisuje set()