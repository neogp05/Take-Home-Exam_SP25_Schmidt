# Lösung 1 a)
# 2
# 1

# Lösung 1 b)
# 9

# Lösung 1 c)
# 2 
# 4 
# 6

# Lösung 1 d)
# 9
# 21





#Lösung 2 a)
x = input("Zahl 1: ")
y = input("Zahl 2: ")

summe = int(x) + int(y)
print("Der Durchschnitt ist:", summe / 2)

# Lösung 2 b)
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 10:
    print("Größer als 10")
elif zahl == 10: 
    print("Genau 10")
else: 
    print("Kleiner als 10")


# Lösung 2 c)
noten = {"Anna": 2, "Ben": 3, "Clara": 1}

print(len(noten))
print(noten.keys())

durchschnitt = sum(noten.values()) / len(noten)
print(durchschnitt)






# Lösung 3 a)
noten = {"Anna": 2, "Ben": 3, "Clara": 1}

print(noten["David"])        # Fehler 1
noten.add("Eva", 2)          # Fehler 2
for key, value in noten.items():
    print(key + ": " + value)   # Fehler 3


#   1. noten["David"], weil der Schlüssel nicht existiert.
#	2. dict.add(...) gibt es nicht; neuen Eintrag mit noten["Eva"] = 2 hinzufügen.	
#   3. key + ": " + value Problem: value ist ein int. Lösung: z.B. print(f"{key}: {value}") oder print(key + ": " + str(value)).



# Lösung 3 b)
zahl = input("Gib eine Zahl ein: ")
if zahl % 2 == 0:                          # Fehler 1
    print("Die Zahl ist gerade")
else:
    print("Die Zahl ist ungerade")

zahlen = [1, 2, 3, 4]
for i in range(5):                        # Fehler 2
    print("Wert:", zahlen[i])

def verdopple(x):
    return x * 2

noten = {"Anna": 1, "Ben": 2}
for name in noten:
    wert = verdopple(noten[name])
    print(name + " hat jetzt Note " + wert)  # Fehler 3

# 	1. input() gibt einen String zurück, der nicht direkt mit % benutzt werden kann.
#	2. range(5) läuft von 0–4, aber zahlen hat nur 4 Elemente (0–3).
#	3. "Note " + wert schlägt fehl, da wert eine Zahl ist und zuerst zu str konvertiert werden muss





# Beispiellösung 4

# globale Variable für Zähler
anzahl_berechnungen = 0

# Funktion zur Durchschnittsberechnung
def durchschnitt(liste):
    global anzahl_berechnungen
    anzahl_berechnungen += 1
    return sum(liste) / len(liste)

# Funktion zur Prüfung
def ist_groesser(liste, grenzwert):
    wert = durchschnitt(liste)
    return wert > grenzwert
