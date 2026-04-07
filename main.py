import csv
from datetime import datetime

bestand = "data.csv"

def schrijf_naar_csv(data):
    try:
        with open(bestand, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        print("Fout bij opslaan:", e)

def vraag_input():
    naam = input("Wat is je naam? ")
    datum = input("Datum (YYYY-MM-DD): ")
    uren = input("Aantal gewerkte uren: ")
    project = input("Aan welk project werkte je? ")

    return [naam, datum, uren, project]

def main():
    print("=== Urenregistratie Systeem ===")

    data = vraag_input()
    schrijf_naar_csv(data)

    print("Gegevens opgeslagen!")

if __name__ == "__main__":
    main()
    