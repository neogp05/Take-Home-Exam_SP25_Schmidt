# Bei diesem Live Code hangelt es sich nicht um direktes Material für den Unterricht, 
# sondern soll nur eine Beispiel darstellen wie es die Lehrkraft machen könnten und enthält
# alle wichtigen Funktionen und Themen die während dem Termin 4 dran kommen sollen 
# Dabei dienen die Kommentare nur zur Verständlichkeit und sollten im spätern Unterricht 
# durch Erklärungen ersetzt werden 


# Funktion ohne Parameter
def sag_hallo():
    print("Hallo, willkommen im Python-Kurs!")

# Aufruf der Funktion
sag_hallo()

# Funktion mit Parameter
def begruessung(name):
    print("Hallo,", name)

begruessung("Lisa")
begruessung("Tom")

# Funktion mit Rückgabewert
def quadriere(x):
    return x * x

ergebnis = quadriere(5)
print("5 zum Quadrat =", ergebnis)

# Funktion mit Standardwert für Parameter
def multiplikation(a, b=2):
    return a * b

print(multiplikation(4))    # b=2 wird automatisch genutzt
print(multiplikation(4, 5)) # b=5 überschreibt den Standardwert


# Nutzung einer globalen Variablen
zähler = 0

def erhöhe_zähler():
    zähler += 1
#    lokale_variable = 3
    print("Zähler:", zähler)

# print(lokale_variable) 
# Fehler!
erhöhe_zähler()
erhöhe_zähler()