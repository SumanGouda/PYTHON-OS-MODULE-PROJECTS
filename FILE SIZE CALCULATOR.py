import os
import tkinter
from tkinter import filedialog

folder = filedialog.askdirectory(title="Select your folder")
for file in os.listdir(folder):
    file_path = os.path.join(folder,file)
    if not os.path.isfile(file_path):
        continue
    size = os.path.getsize(file_path)
    size_kb = size / 1024
    rounded_kb = round(size_kb,2)
    print(file," kb" ,end=" ")
    print(size_kb," kb")
        