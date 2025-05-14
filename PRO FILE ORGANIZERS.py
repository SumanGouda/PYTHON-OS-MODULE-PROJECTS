
import tkinter as tk
import os
import shutil
import sys
from tkinter import filedialog
from tkinter import Tk

class FileManager:
    def __init__(self):
        self.folder_path = ""
        Tk().withdraw()

    def organize_folder(self):
        self.folder_path = filedialog.askdirectory(title= "Select the folder")
        if not self.folder_path:
            print("No folder selected")
            return
        
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            
            if os.path.isdir(file_path):
                continue
            
            _, ext = os.path.splitext(file)
            ext = ext[1:]
            
            new_folder = os.path.join(self.folder_path, ext)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
                
            shutil.move(file_path,new_folder)
            
    def delete_file(self):
        file_delete = filedialog.askdirectory(title="Select the folder or file you want to delete")
        if not file_delete :
            print("No folder selected")
            return
        
        confirm = input(f"Are you sure you want to delete this folder?\n{file_delete}\nType 'yes' to confirm: ")
        if confirm.lower() == "yes":
            try:
                shutil.rmtree(file_delete)
                print("File deleted succesfully.")
            except Exception as e:
                print("Error in deleting file: ",e)
        else:
            print("File deletion cancelled.")
            
    def get_folder_summary(self):
        select_folder = filedialog.askdirectory(title="Select your folder")
        if not select_folder:
            print("No folder selected.")
            return
        
        list_folder = {"Subfolder" : (0,0)} 
        
        for file in os.listdir(select_folder):
            file_path = os.path.join(select_folder,file)
            file_size = os.path.getsize(file_path) / 1024
            rounded_file_size = round(file_size,2)
            
            if os.path.isdir(file_path) :
                current_count, current_size = list_folder["Subfolder"]
                list_folder["Subfolder"] = (current_count + 1, current_size + rounded_file_size)
            
            else:
                _,ext = os.path.splitext(file)
                if ext in list_folder:
                    current_count, current_size = list_folder[ext]
                    list_folder[ext] = (current_count + 1, current_size + rounded_file_size)
                elif ext not in list_folder:
                    list_folder[ext] = (1, rounded_file_size)
            
        print("Folder Summary:\n")
        for ext, (count, size) in list_folder.items():
            print(f"{ext:15} --> {count} files | {size:.2f} KB")

def run_gui():
    fm = FileManager()
    
    root = tk.Tk()
    root.title("File Manager")
    root.geometry("300x200")
    
    tk.Button(root, text= "Organize Folder", width = 25, command=fm.organize_folder).pack(pady=10)
    tk.Button(root, text="Delete Folder", width=25, command=fm.delete_file).pack(pady=10)
    tk.Button(root, text= "Get Folder Summary", width=25,command=fm.get_folder_summary).pack(padx=10)
    
    root.mainloop()
    
run_gui()
        
                    
                
                
            
        
            
        
