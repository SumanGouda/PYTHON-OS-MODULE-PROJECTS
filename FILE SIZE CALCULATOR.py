import os
import tkinter
from tkinter import filedialog

folder = filedialog.askdirectory(title="Select your folder")
    #Opens the file manager window that allows the user to select folder

if not folder:
    print("No folder selected.")
    exit()

for file in os.listdir(folder):
        #Makes a list of all the files in the folder
    file_path = os.path.join(folder,file)
    if not os.path.isfile(file_path):
        #Skip the subfolder inside the folder 
        continue
    
    size_kb = os.path.getsize(file_path) / 1024
    rounded_kb = round(size_kb,2)
    print(file," KB" ,end=" ")
    print(rounded_kb," KB")
        
