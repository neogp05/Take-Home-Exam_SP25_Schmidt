# Basisklasse Hund
class Hund:
    tierart = "Hund"  # Klassenvariable

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter  # Attribute

    def laut_geben(self, ton="Wuff", anzahl=1):
        print((ton + " ") * anzahl)

    def beschreibe(self):
        print(f"{self.name} ist {self.alter} Jahre alt.")

# Unterklasse Welpe erbt von Hund
class Welpe(Hund):
    def __init__(self, name, alter, lieblingsspielzeug):
        super().__init__(name, alter)  # Vererbung der Attribute
        self.lieblingsspielzeug = lieblingsspielzeug  # neues Attribut

    def laut_geben(self, ton="Wau", anzahl=1):  # Methode überschreiben
        print((ton + " ") * anzahl)

    def spiel(self):
        print(f"{self.name} spielt gerne mit {self.lieblingsspielzeug}.")

# Objekte erstellen
hund1 = Hund("Bello", 5)
welpe1 = Welpe("Fips", 1, "Ball")

# Methoden aufrufen
hund1.laut_geben()
hund1.beschreibe()

welpe1.laut_geben(anzahl=3)
welpe1.beschreibe()
welpe1.spiel()

# Liste von Objekten und Schleife
tiere = [hund1, welpe1]
for tier in tiere:
    tier.laut_geben(anzahl=2)