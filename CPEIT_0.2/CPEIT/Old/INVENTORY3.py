import tkinter as tk
from tkinter import messagebox
import subprocess
import json

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("xtool")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello! Welcome to xtool!")
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Proceed", command=self.show_methods)
        self.button.pack(padx=10, pady=10)

    def show_methods(self):
        self.label.pack_forget()
        self.button.pack_forget()

        self.label = tk.Label(self, text="Select the methods to build inventory:")
        self.label.pack(padx=10, pady=10)

        self.get_package_var = tk.BooleanVar()
        self.get_package_checkbutton = tk.Checkbutton(self, text="Get-Package", variable=self.get_package_var)
        self.get_package_checkbutton.pack(padx=10, pady=5, anchor=tk.W)

        self.get_item_var = tk.BooleanVar()
        self.get_item_checkbutton = tk.Checkbutton(self, text="Get-Item", variable=self.get_item_var)
        self.get_item_checkbutton.pack(padx=10, pady=5, anchor=tk.W)

        self.get_wmiobject_var = tk.BooleanVar()
        self.get_wmiobject_checkbutton = tk.Checkbutton(self, text="Get-WmiObject", variable=self.get_wmiobject_var)
        self.get_wmiobject_checkbutton.pack(padx=10, pady=5, anchor=tk.W)

        self.psutil_var = tk.BooleanVar()
        self.psutil_checkbutton = tk.Checkbutton(self, text="psutil", variable=self.psutil_var)
        self.psutil_checkbutton.pack(padx=10, pady=5, anchor=tk.W)

        self.gather_button = tk.Button(self, text="Gather", command=self.gather_results)
        self.gather_button.pack(padx=10, pady=10)

    def gather_results(self):
        if not self.get_package_var.get() and not self.get_item_var.get() and not self.get_wmiobject_var.get() and not self.psutil_var.get():
            messagebox.showerror("Error", "Please select at least one option.")
            return

        if self.get_package_var.get():
            subprocess.call(["powershell.exe", "-File", "Get-Package.ps1"])
            with open("packages.json", "r") as f:
                package_data = json.load(f)

        if self.get_item_var.get():
            subprocess.call(["powershell.exe", "-File", "Get-Item.ps1"])
            with open("item.json", "r") as f:
                item_data = json.load(f)

        if self.get_wmiobject_var.get():
            subprocess.call(["powershell.exe", "-File", "Get-WmiObject.ps1"])
            with open("wmiobject.json", "r") as f:
                wmiobject_data = json.load(f)

        if self.psutil_var.get():
            subprocess.call(["python", "psutil.py"])
            with open("psutil.json", "r") as f:
                psutil_data = json.load(f)

        self.label.pack_forget()
        self.get_package_checkbutton.pack_forget()
