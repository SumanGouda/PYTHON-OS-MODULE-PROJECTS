import _tkinter
import os
from tkinter import filedialog

folder = filedialog.askdirectory(title="Select your folder")
file_list = []

if not folder:
    print("No folder selected")
    exit()

for file in os.listdir(folder):
    file_path = os.path.join(folder,file)
    if not os.path.isfile(file_path):
        continue

    size = os.path.getsize(file_path)
    file_list.append((file,size))

sorted_list = sorted(file_list, key = lambda x: x[1], reverse = True)

for filename, size in sorted_list:
    print(f"{filename}: {round(size/1024, 2)} KB")
    

    
    
    