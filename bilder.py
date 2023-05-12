# Crea un programa que obtenga los archivos de las carpetas de un directorio.
# Si el nombre de la carpeta termina en _fav, guarda esas fotos en dos carpetas, en la general y en la del album.
# Renombra los archivos con el nombre de la carpeta. 
# Si el formato del archivo es de video y es de más de 200 mb copia el nombre del archivo en un excel.

import os
import shutil
#from openpyxl import Workbook

# Katalogen hvor mappene ligger
directory = 'C:/Users/admin/Pictures/Prueba'

# Opprett en Excel-fil
#wb = Workbook()
#ws = wb.active
#ws.title = "Store videoer"
#os.makedirs(os.path.join(directory, "generell"))

def reemplazar_caracter(cadena):
    nueva_cadena = cadena.replace('\\', '/')
    return nueva_cadena

# Gå gjennom alle filene og mappene i katalogen
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Sjekk om filen er en mappe og om den ender med "_fav"
    if os.path.isdir(filepath):
        # Opprett to nye mapper, én for generelle bilder og én for albumet
        #os.makedirs(os.path.join(directory, "generell", filename))
        #os.makedirs(os.path.join(directory, "album", filename))
        
        # Gå gjennom alle filene i mappen
        for file in os.listdir(filepath):
            file_path = os.path.join(filepath, file)
            #print(file_path)
            #print(filename)
            file_path = reemplazar_caracter(file_path)
            #print("Source: " + file_path)
            #print(file)
            #print(os.path.join(directory, "generell", filename, file))
            destination = reemplazar_caracter(os.path.join(directory, "generell", file))
            #
            #print("Destination: " + destination)
            # Sjekk om filen er et bilde
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                # Kopier bildet til både den generelle og album-mappen
                if not os.path.exists(destination):
                    shutil.copy(file_path, destination)
                    print("P Filen kopiert")
                else:
                    print("P Filen eksisterer fra før")
                #shutil.copy(file_path, os.path.join(directory, "album", filename, file))
                
                # Gi filen et nytt navn med navnet på mappen
                # os.rename(os.path.join(directory, "generell", filename, file), os.path.join(directory, "generell", filename, filename + "." + file.split(".")[-1]))
                #os.rename(os.path.join(directory, "album", filename, file), os.path.join(directory, "album", filename, filename + "." + file.split(".")[-1]))
            
            # Sjekk om filen er en video og om den er større enn 200 mb
            elif file.lower().endswith((".mp4", ".avi", ".mov")):
                # if os.path.getsize(file_path) > 200 * 1024 * 1024:
                if not os.path.exists(destination):
                    shutil.copy(file_path, destination)
                    print("V Filen kopiert")
                else:
                    print("V Filen eksisterer fra før")
                    # Skriv navnet på videoen til Excel-filen
                    #ws.append([file])
             
    
# Lagre Excel-filen
# wb.save(os.path.join(directory, "store_videoer.xlsx"))