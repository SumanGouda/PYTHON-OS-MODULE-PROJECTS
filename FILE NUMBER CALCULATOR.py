import os
import tkinter
from tkinter import filedialog

folder = filedialog.askdirectory(title="Select your folder")

if not folder:
    print("No folder selected.")
    exit()
 
track = {"Subfolder":0} 

for file in os.listdir(folder):
    file_path = os.path.join(folder,file)
    if os.path.isdir(file_path):
        track["Subfolder"] += 1
        continue
    
    _, ext = os.path.splitext(file_path)
    if ext in track:
        track[ext] += 1
    else:
        track[ext] = 1

for key, value in track.items():
    print(f"{key}: {value}")       

    
    
    