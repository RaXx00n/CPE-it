import tkinter as tk
import subprocess

class XToolGUI:
    def __init__(self, master):
        self.master = master
        master.title("XTool")
        
        self.label1 = tk.Label(master, text="Hello! Welcome to XTool!")
        self.label1.pack()
        
        self.button1 = tk.Button(master, text="Proceed", command=self.create_second_screen)
        self.button1.pack()
    
    def create_second_screen(self):
        self.label1.destroy()
        self.button1.destroy()
        
        self.label2 = tk.Label(self.master, text="Select the methods to build inventory:")
        self.label2.pack()
        
        self.var1 = tk.BooleanVar()
        self.check1 = tk.Checkbutton(self.master, text="Get-Package", variable=self.var1)
        self.check1.pack()
        
        self.var2 = tk.BooleanVar()
        self.check2 = tk.Checkbutton(self.master, text="Get-Item", variable=self.var2)
        self.check2.pack()
        
        self.var3 = tk.BooleanVar()
        self.check3 = tk.Checkbutton(self.master, text="Get-WmiObject", variable=self.var3)
        self.check3.pack()
        
        self.var4 = tk.BooleanVar()
        self.check4 = tk.Checkbutton(self.master, text="psutil", variable=self.var4)
        self.check4.pack()
        
        self.button2 = tk.Button(self.master, text="Gather", command=self.run_scripts)
        self.button2.pack()
    
    def run_scripts(self):
        if self.var1.get():
            subprocess.call(["powershell", "Get-Package.ps1"])
        if self.var2.get():
            subprocess.call(["powershell", ".\Get-Item.ps1"])
        if self.var3.get():
            subprocess.call(["powershell", "Get-WmiObject.ps1"])
        if self.var4.get():
            subprocess.call(["python", "psutil.py"])

root = tk.Tk()
my_gui = XToolGUI(root)
root.mainloop()
