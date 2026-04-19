import pandas as pd
import os

# Pfade
csv_ordner = "csv"
excel_ordner = "excel"

# Zielordner erstellen (falls nicht vorhanden)
os.makedirs(excel_ordner, exist_ok=True)

# Alle Dateien im CSV-Ordner durchgehen
for datei in os.listdir(csv_ordner):
    if datei.endswith(".csv"):
        csv_pfad = os.path.join(csv_ordner, datei)
        
        # CSV einlesen
        df = pd.read_csv(csv_pfad)
        
        # Neuer Dateiname (csv → xlsx)
        excel_name = datei.replace(".csv", ".xlsx")
        excel_pfad = os.path.join(excel_ordner, excel_name)
        
        # Als Excel speichern
        df.to_excel(excel_pfad, index=False)

print("Fertig! Alle CSV-Dateien wurden konvertiert.")