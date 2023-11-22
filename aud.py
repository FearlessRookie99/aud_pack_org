import csv


def load_packs(capacity, csv_file):
    packs = []

    # CSV-Datei wird importiert 
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  #Spaltennamen werden hier übersprungen 

        # einzelne Elemente werden extrahiert und in einer Liste eingefügt
        for row in reader:
            pack_number = int(row[0])
            volume = float(row[1])
            price = float(row[2])
            rate = price / volume 
            packs.append((pack_number, volume, price,rate))

    #  liste wird sortiert anhand rate price/volume  
    sorted_packs = sorted(packs, key=lambda pack: pack[3], reverse=True)
  
    #datenfelder 
    total_volume = 0
    total_price = 0
    prioritized_packs = []

    #liste wird untersucht und Pakete werden priorisiert in einer Liste hinzugefügt
    for pack in sorted_packs:
        if total_volume + pack[1] <= capacity:
            prioritized_packs.append(pack[0])
            total_volume += pack[1]
            #Rechnung der insgesamt erzielte Umsatz
            total_price += pack[2]
    
    #stehen bleibende Pakete werden in einer Liste hinzugefügt 
    remaining_packs = [pack[0] for pack in sorted_packs if pack[0] not in prioritized_packs]

    return prioritized_packs, total_price, remaining_packs

# Eingabe der verfügbaren Kapazität 
while True:
    try:
        capacity = float(input("Bitte geben Sie das maximale Ladevolumen ein: "))
        break
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine numerische Zahl ein.")



#Eingabe der CSV datei als Pfad  
while True:
    try:
        csv_file = input("Bitte geben Sie den relativen Dateipfad(ordner/datei) zur CSV-Datei ein: ")
        with open(csv_file, 'r') as file:
            break
    except FileNotFoundError:
        print("Datei nicht gefunden. Bitte überprüfen Sie den Dateipfad.")


# Aufruf der Funktion um das Programm durchzulafen 
prioritized_packs, total_price, remaining_packages = load_packs(capacity , csv_file)

# Ausgabe der priorisierten Pakete
print("Priorisierte Pakete:", prioritized_packs)
# Ausgabe des Gesamt erzielten Umsatzes
print("Gesamtpreis:", total_price, "Euro")
# Ausgabe  der übrigen Pakete
print("Übrige Pakete:", remaining_packages)
