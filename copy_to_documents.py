import os
import shutil

file1 = "D:/Path-of-Exile-Filter-Backup/Book of Wisdom.filter"
file2 = "D:\Documents\My Games\Path of Exile\Book of Wisdom.filter"

# Vergleiche die Änderungszeiten der beiden Dateien
#if os.path.getmtime(file1) < os.path.getmtime(file2):
    # Kopiere die neuere Datei in den Ordner
    #shutil.copy2(file2, file1)
    #print(f"{file2} was copied to {file1}")
if os.path.getmtime(file1) > os.path.getmtime(file2):
    # Kopiere die ältere Datei in den Ordner
    shutil.copy2(file1, file2)
    print(f"{file1} was copied to {file2}")
else:
    # Keine der beiden Dateien ist neuer als die andere
    raise ValueError("Both files have the same modification time")
