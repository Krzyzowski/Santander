owoce = ["jabłko", "banan", "pomarańcza"]


for owoc in owoce:
    print(owoc)

print( )

licznik = 0

while licznik < 5:

    
    print(licznik)
    licznik += 1

print( )
licznik = 0


while True:
    #licznik += 1
    print(licznik)
    licznik += 1


    if licznik == 6:
        break

print( )
print("continue")
for i in range(10):

    if i % 2 != 0:
        continue
    print(i)