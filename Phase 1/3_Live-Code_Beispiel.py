# Bei diesem Live Code hangelt es sich nicht um direktes Material für den Unterricht, 
# sondern soll nur eine Beispiel darstellen wie es die Lehrkraft machen könnten und enthält
# alle wichtigen Funktionen und Themen die während dem Termin 3 dran kommen sollen 
# Dabei dienen die Kommentare nur zur Verständlichkeit und sollten im spätern Unterricht 
# durch Erklärungen ersetzt werden 


# Listen erstellen und bearbeiten
farben = ["rot", "blau", "grün"]  # Liste anlegen
print(farben)                      # Ganze Liste ausgeben

farben.append("gelb")              # Element hinzufügen
farben.remove("blau")              # Element entfernen

for farbe in farben:               # Schleife über Liste
    print(f"Ich mag die Farbe {farbe}")

# Länge der Liste herausfinden
print(f"Die Liste hat {len(farben)} Farben")

# Dictionary erstellen und bearbeiten
noten = {"Anna": 1, "Ben": 2, "Clara": 3}  # Schlüssel-Wert-Paare
print(noten)

noten["Daniel"] = 2                         # Neues Paar hinzufügen
noten["Anna"] = 2                            # Wert ändern

for schueler, note in noten.items():        # Schleife über Dictionary
    print(f"{schueler} hat die Note {note}")

# Zugriff auf einzelne Elemente
print(f"Annas Note: {noten['Anna']}")