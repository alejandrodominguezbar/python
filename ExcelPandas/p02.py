# Importer biblioteker
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np


# Create a root window
root = tk.Tk()
root.withdraw()


inform = messagebox.askquestion("Info","Select and Excel file")

# Ask the user to select a file
file_path = filedialog.askopenfilename()
df = pd.read_excel(file_path)
# Skriv ut hele dataframen
print(df)
# Legg til nye kolonner 
df["Pris"] = np.nan
df["PrecioFijo"] = 35
df["PrecioTotal"] = df["PrecioFijo"] * df["Kostnader"]
df["K2"] = df["PrecioTotal"] / df["PrecioFijo"]
df['compare'] = df['Kostnader'] == df['K2']

# Skriv ut hele dataframen
print(df)

# Print the selected file path
print("Selected file:", file_path)
# Ask the user a yes or no question
result = messagebox.askyesno("Question", "Do you want to save?")

# Print the user's response
if result:
    print("User clicked Yes")
    df.to_excel('filep02output.xlsx', index=False)
else:
    print("User clicked No")