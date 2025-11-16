import datetime                                                                                 # Import von Datum inkl. Uhrzeit
import os                                                                                       # Import v. Betriebssystem-Modul zur Prüfung der CSV-Dateigröße (für Header-Erstellung oder nicht)
datum = datetime.date.today()                                                                   # Anpassung das nur das Datum von heute genommen wird
datum_form = datum.strftime("%d.%m.%y")                                                         # Datumsformat festgelegt auf TT.MM.JJJJ
price = 0.2916                                                                                  # Variable f. den Preis
while True:                                                                                     # Start der while-Schleife
    try:                                                                                        # Beginn der try...exept Bedingung
        kWh = float (input (f"\nWie viel kWh wurden erzeugt? "))                                # Frage um die kWh zu erhalten inkl. Umwandlung von String zu Float.
        print (f"\nAm {datum_form} beträgt die Strompreis-Ersparnis: {price * kWh :.2f}€ \n")   # Ausgabe vom Ergebnis mit max zwei Stellen hinterm Komma (Variable:.2f) u. Zeilenumbruch dank \n
        if not os.path.exists('historie.csv') or os.path.getsize('historie.csv') == 0:          # If-Schleife zum Prüfen ob CSV-Datei vorhanden oder leer f. Header
            header_needed = True                                                                # Variable auf "true" zwecks Header-Erstellung 
        else:                                                                                   # Else-Bedingung falls Header bereits vorhanden ist
            header_needed = False                                                               # Variable auf "false" zwecks Header-Erstellung 
        daten_expo = f"{datum_form}; {kWh:.2f}; {price * kWh :.2f}"                             # Iteration einer Variable um einen String in eine CSV-Datei zu exportieren
        with open("historie.csv", "a") as datei:                                                # Datei "historie.csv" erstellen oder öffnen uu. Text einfügen am Ende ("a")
            if header_needed:                                                                   # Wenn Header benötigt dann tue dies
                datei.write("Datum; kWh; Ersparnis in €\n")                                     # Einfügen des Headers wenn Datei neu oder leer ist
            datei.write(daten_expo + "\n")                                                      # Schreibprozess inkl. Zeilenumbruch (\n)
        break                                                                                   # break um die while-Schleife zu beenden bei korrekter Eingabe
    except ValueError:                                                                          # except greif wenn keine Zahl eingegeben wird
        print (f"\nFehler: Gibt bitte nur  Zahlen ein\n")                                       # Ausgabe wenn z. B. ein Buchstabe getippt wird da float nur Zahlen erkennt
input ("Drücke ENTER, zum Schließen des Fensters.")                                             # Eingebaute Pause damit die Datei sich nicht einfach schließt