"""                                                     
Homelab Service Monitor - Raspberry Pi Service Monitoring

Überwacht kritische Services (Nextcloud, Pi-hole, Tailscale) und 
generiert automatisch Alarme bei Problemen.

Autor: Dave
Datum: 07.11.2025
Version: 1.0
"""

# Import u. Formatierung v. Datum
from datetime import datetime
# Defnition wie das DAtum aussehen soll 
datum_form = datetime.now().strftime("%d.%m.%y um %H:%M:%S Uhr")

# Dictionary defnieren mit Name und Parametern
services = {                                     
    "Nextcloud": {                                      
        "cpu": 42,                                      
        "ram": 212,                                    
        "laufzeit": 99.8,
        "status": "aktiv"
    },
    "Pi-hole": {
        "cpu": 12,
        "ram": 128,
        "laufzeit": 99.9,
        "status": "aktiv"
    },
    "Tailscale": {
        "cpu": 82,
        "ram": 226,
        "laufzeit": 92.2,
        "status": "aktiv"
    }
}

# Funktionen f. mehrere Bereiche zwecks Optik
def kopf():
    """Zeigt den Header für Tests."""
    print("\n" + "="*58)
    print(" ausgelagerter Test-Bereich - Homelab Monitor ".center(58, "="))                                  
    print("="*58)
    print(" Service-Check-Test ".center(58, "="))           
    print("="*58)
    print("="*2 + "".center(54) + "="*2)
    
def alarm ():
    """Zeigt d. Header f. Alarm-Test."""
    print("="*58)
    print(" Alarm-Test ".center(58, "="))
    print("="*58)
    print("="*2 + "".center(54) + "="*2)
def durch():
    """Zeigt d. Header f. Durchschnitts-Test."""
    print("="*2 + "".center(54) + "="*2)
    print("="*58)
    print(" Durchschnitts-Test ".center(58, "="))
    print("="*58)
    print("="*2 + "".center(54) + "="*2)
def head_alles():
    """Zeigt d. Header f. "alles_zeigen"-Bereich"""
    print("\n" + "="*58)
    print(" Homelab-Service-Monitor ".center(58, "="))
    print("="*58)
def ende():
    """Zeigt die End-Zeile des Tests."""
    input(" Drücke ENTER zum Beenden ".center(58, "="))  
    
def service_check(service_name, service_daten):
    """
    Checkt ob ein Service Probleme hat oder alles OK ist.
    
    Die Funktion schaut sich CPU, RAM und Laufzeit an:
        - CPU über 80%? → Problem!
        - RAM über 1000 MB? → Problem!
        - Laufzeit unter 95%? → Problem!
    
    Was braucht die Funktion?
        service_name: Der Name vom Service (z.B. "Nextcloud")
        service_daten: Das Dictionary mit den Werten (cpu, ram, laufzeit)
    
    Was kommt raus?
        Entweder "OK" oder "WARNUNG"
    
    Beispiel:
        status = service_check("Nextcloud", services["Nextcloud"])
        # Gibt "OK" oder "WARNUNG" zurück
    """
    # Werte aus dem "services" Dictonary holen
    cpu = service_daten ["cpu"]
    ram = service_daten ["ram"]
    laufzeit = service_daten ["laufzeit"]

    # If-Schleife um zu kontrollieren ob OK oder WARUNUNG erforderlich
    # CPU-Auslastung kontrollieren (kritisch ab 80%)
    if cpu > 80:
        return "WARNUNG"
    # RAM-Nutzung kontrollieren (kritisch ab 1000 MB)
    elif ram > 1000:
        return "WARNUNG"
    # Laufzeit kontrollieren (kritisch unter 95%)
    elif laufzeit < 95:
        return "WARNUNG"
    # Ausgabe wenn alles im grünen Bereich ist
    else:
        return "OK"

# Globale Liste für Alarm-Historie (wird durch alarm_generator befüllt)  
alarm_historie = []

# Alarm-Generator inkl. aktuellem Datum
def alarm_generator (service_name, grund):
    """
    Erstellt einen neuen Alarm wenn was schief läuft.
    
    Was macht die Funktion?
        1. Baut ein Dictionary mit Service-Name, Grund und Datum
        2. Packt diesen Alarm in die alarm_historie Liste
        3. Gibt eine Warnung auf dem Bildschirm aus
    
    Was braucht die Funktion?
        service_name: Welcher Service hat das Problem? (z.B. "Pi-hole")
        grund: Was ist das Problem? (z.B. "CPU zu hoch (85%)")
    
    Wichtig:
        Diese Funktion verändert die globale alarm_historie Liste!
        Jeder Aufruf fügt einen neuen Alarm hinzu.
    
    Beispiel:
        alarm_generator("Tailscale", "CPU-Auslastung kritisch (82%)")
        # Alarm wird gespeichert und angezeigt
    """
    alarm = {
    "Service": service_name,
    "Grund": grund,
    "Datum": datum_form
}
    alarm_historie.append(alarm)
    print("="*2 + f"ALARM: {service_name} - {grund}".center(54) + "="*2)

# Durchschnittswerte werden generiert f. Ausgabe weiter unten
def durchschnitt ():
    """
    Rechnet den Durchschnitt von CPU und RAM über alle Services aus.
    
    Wie funktioniert's?
        1. Geht durch alle Services mit einer Schleife
        2. Addiert alle CPU-Werte zusammen
        3. Addiert alle RAM-Werte zusammen
        4. Teilt durch die Anzahl der Services = Durchschnitt!
    
    Was kommt raus?
        Zwei Werte in Klammern (das nennt man "Tuple"):
        - Erster Wert: Durchschnitt CPU in Prozent
        - Zweiter Wert: Durchschnitt RAM in MB
    
    Beispiel:
        durch_cpu, durch_ram = durchschnitt()
        # durch_cpu könnte z.B. 45.3 sein
        # durch_ram könnte z.B. 188.7 sein
    """
    total_cpu = 0
    total_ram = 0
    count = 0

    # Services werden per Schleife gecheckt
    for service_name, service_daten in services.items():
        total_cpu += service_daten["cpu"]
        total_ram += service_daten["ram"]
        count += 1

    durch_cpu = total_cpu / count
    durch_ram = total_ram / count
    return durch_cpu, durch_ram

# Finale Test-Funktion
def alles_zeigen():
    """
    Die Hauptfunktion - zeigt das komplette Dashboard mit allem drum und dran!
    
    Was wird alles angezeigt?
        - Jeden Service einzeln (Name, CPU, RAM, Laufzeit)
        - Status von jedem Service (OK oder WARNUNG)
        - Durchschnittswerte über alle Services
        - Wie viele Alarme es gibt
        - Details zu allen Alarmen (wenn welche da sind)
    
    Besonderheit:
        Diese Funktion ruft auch alarm_generator() auf, wenn ein Service
        kritische Werte hat. Das heißt, Alarme werden hier automatisch erstellt!
    
    Ablauf:
        1. Geht mit einer Schleife durch alle Services
        2. Zeigt die Werte von jedem Service an
        3. Checkt mit service_check() ob alles OK ist
        4. Erstellt Alarme wenn nötig
        5. Zeigt am Ende die Durchschnittswerte
        6. Zeigt alle Alarme an (falls vorhanden)
    """
    # Durch alle Services gehen per Schleife
    for service_name, service_daten in services.items():
        # Service-Namen ausgeben
        print("="*2 + "".center(54) + "="*2)
        print("="*2 + f"Service: {service_name}".center(54) + "="*2)
        
        # Metriken ausgeben
        cpu = service_daten["cpu"]
        ram = service_daten["ram"]
        laufzeit = service_daten["laufzeit"]
        
        print("="*2 + f"  CPU: {cpu}%".center(54) + "="*2)
        print("="*2 + f"  RAM: {ram}MB".center(54) + "="*2)
        print("="*2 + f"  Laufzeit: {laufzeit}%".center(54) + "="*2)
        
        # Status checken
        status = service_check(service_name, service_daten)
        
        # Status anzeigen
        if status == "OK":
            print("="*2 + "  Status: OK".center(54) + "="*2)
        else:
            print("="*2 + "  Status: WARNUNG".center(54) + "="*2)
            # Alarm generieren!
            if cpu > 80:
                alarm_generator(service_name, f"CPU-Auslastung kritisch ({cpu}%)")
            if ram > 1000:
                alarm_generator(service_name, f"RAM-Nutzung kritisch ({ram}MB)")
            if laufzeit < 95:
                alarm_generator(service_name, f"Laufzeit kritisch ({laufzeit}%)")
        
        print("="*2 + "".center(54) + "="*2)
        print("="*58
)

        # Gesamtauslastung anzeigen
    durch_cpu, durch_ram = durchschnitt()
    print("="*2 + "".center(54) + "="*2)
    print("="*2 + " Gesamtauslastung ".center(54) + "="*2)
    print("="*2 + f"Durchschnitt CPU: {durch_cpu:.1f}%".center(54) + "="*2)
    print("="*2 + f"Durchschnitt RAM: {durch_ram:.0f}MB".center(54) + "="*2)
    
    # Alarm-Anzahl
    print("="*2 + "".center(54) + "="*2)
    print("="*2 + f"Alarme: {len(alarm_historie)}".center(54) + "="*2)
    print("="*2 + "".center(54) + "="*2)
    
    print("="*58)

    #Alarm-Details
    if len(alarm_historie) > 0:
        print("="*2 + "".center(54) + "="*2)
        print("="*2 + " Alarm-Liste ".center(54) + "="*2)
        for alarm in alarm_historie:
            print("="*2 + f"{alarm['Service']}: {alarm['Grund']}".center(54) + "="*2)
            print("="*2 + f"Datum: {alarm['Datum']}".center(54) + "="*2)
            print("="*2 + "".center(54) + "="*2)
        print("="*58
)

# Testbereich m. zentrierter Ausgabe
if __name__ == "__main__":
    head_alles()
    alles_zeigen()
    ende()