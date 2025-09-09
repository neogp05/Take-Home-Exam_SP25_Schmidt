# Bei diesem Live Code hangelt es sich nicht um direktes Material für den Unterricht, 
# sondern soll nur eine Beispiel darstellen wie es die Lehrkraft machen könnten und enthält
# alle wichtigen Funktionen und Themen die während dem Termin 1 dran kommen sollen 
# Dabei dienen die Kommentare nur zur Verständlichkeit und sollten im spätern Unterricht 
# durch Erklärungen ersetzt werden 


# Erstes Programm "Hello World"
print("Hello World")

# Eingabe 
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
# Input erzeugt immer automatisch einen String 
# int() um in ganzahl umzuwandeln 

# Verarbeitung
naechstes_jahr = alter + 1

# Ausgabe
print("Hallo", name + "!")
print(f"Nächstes Jahr wirst du {naechstes_jahr} Jahre alt.")



# Beispiel Taschenrechner 
zahl1 = input("Bitte gib die erste Zahl ein: ")
zahl2 = input("Bitte gib die zweite Zahl ein: ")

# Typumwandlung (String -> Zahl)
zahl1 = float(zahl1)
zahl2 = float(zahl2)
# float() für Kommazahl

# Grundrechenarten
print("Addition:", zahl1 + zahl2)
print("Subtraktion:", zahl1 - zahl2)
mult = zahl1 * zahl2
print("Multiplikation:", mult)
div = zahl1 / zahl2
print("Division:", div)

# Weitere Operatoren
print("Ganzzahlige Division:", zahl1 // zahl2)
print("Rest (Modulo):", zahl1 % zahl2)
print("Potenz:", zahl1 ** zahl2)

# Kommentare erklären
# Das ist ein Kommentar -> wird vom Programm ignoriert
# Hier könnte man weitere Operationen ergänzen

