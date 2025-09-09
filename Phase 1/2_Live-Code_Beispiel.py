# Bei diesem Live Code hangelt es sich nicht um direktes Material für den Unterricht, 
# sondern soll nur eine Beispiel darstellen wie es die Lehrkraft machen könnten und enthält
# alle wichtigen Funktionen und Themen die während dem Termin 2 dran kommen sollen 
# Dabei dienen die Kommentare nur zur Verständlichkeit und sollten im spätern Unterricht 
# durch Erklärungen ersetzt werden 

# ------ Vergleichsoperatoren ------
a = 5
b = 3
print("a =", a, ", b =", b)
print("a == b:", a == b)   # gleich
print("a != b:", a != b)   # ungleich
print("a < b :", a < b)    # kleiner
print("a > b :", a > b)    # größer
print("a <= b:", a <= b)   # kleiner oder gleich
print("a >= b:", a >= b)   # größer oder gleich



# ------ Bedingung ------
# Beispiel: gerade oder ungerade
zahl = int(input("Gib eine Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")



# ------ Schleifen ------
# for-Schleife
for i in range(1, 6):  # Zahlen 1 bis 5
    print("Zahl:", i)


# while-Schleife
x = 1
while x <= 5:
    print("Zähler:", x)
    x += 1


# Beispiel Teilbarkeit 
for i in range(1, 11):
    if i % 3 == 0:
        print(i, "ist durch 3 teilbar")
    else:
        print(i, "ist nicht durch 3 teilbar")


# Schleife mit break
for i in range(1, 11):
    if i == 5:
        print("Abbruch bei Zahl 5")
        break
    print("Zahl:", i)
# break beendet Schleife

# Schleife mit continue
for i in range(1, 6):
    if i == 3:
        print("Überspringe die 3")
        continue
    print("Zahl:", i)
# continue überspringt aktuelle Iteration 