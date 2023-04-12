#Import library
import pandas as pd

#Excel file must be in the same folder
df = pd.read_excel("Excel Python.xlsx") 


print(df.Navn)


i = 0
j= 0
for ind in df.index:
    j = j + (df['KundeID'][ind])
    i = i + 1


print (i)
print (j)