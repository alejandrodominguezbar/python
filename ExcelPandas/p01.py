# Importer biblioteker
import pandas as pd
import numpy as np

# Les Excel-fil 
df = pd.read_excel("Excel Python.xlsx")

# Legg til nye kolonner 
df["Pris"] = np.nan
df["PrecioFijo"] = 35
df["PrecioTotal"] = df["PrecioFijo"] * df["KundeID"]
df["K2"] = df["PrecioTotal"] / df["PrecioFijo"]
df['compare'] = df['KundeID'] == df['K2']

# Skriv ut hele dataframen
print(df)

# Beregn summen av alle verdiene 'KundeID'
# og antallet rader i dataframen
i = 0
j = 0
for ind in df.index:
    j = j + (df['KundeID'][ind])
    i = i + 1

# Skriv ut 
# print(i)
# print(j)