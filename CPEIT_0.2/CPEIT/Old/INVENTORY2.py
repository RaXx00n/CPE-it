import tkinter as tk
import subprocess

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("xtool")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        # First screen
        self.label1 = tk.Label(self, text="Hello! Welcome to xtool!")
        self.label1.pack(pady=20)
        self.button1 = tk.Button(self, text="Proceed", command=self.show_second_screen)
        self.button1.pack()

    def show_second_screen(self):
        # Second screen
        self.label1.destroy()
        self.button1.destroy()
        self.label2 = tk.Label(self, text="Select the methods to build inventory")
        self.label2.pack(pady=10)
        self.var1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self, text="Get-Package", variable=self.var1)
        self.check1.pack()
        self.var2 = tk.IntVar()
        self.check2 = tk.Checkbutton(self, text="Get-Item", variable=self.var2)
        self.check2.pack()
        self.var3 = tk.IntVar()
        self.check3 = tk.Checkbutton(self, text="Get-WmiObject", variable=self.var3)
        self.check3.pack()
        self.var4 = tk.IntVar()
        self.check4 = tk.Checkbutton(self, text="psutil", variable=self.var4)
        self.check4.pack()
        self.button2 = tk.Button(self, text="Gather", command=self.show_third_screen)
        self.button2.pack(pady=20)

    def show_third_screen(self):
        # Third screen
        selected_options = []
        if self.var1.get() == 1:
            subprocess.call(["powershell.exe", ".\Get-Package.ps1"])
            selected_options.append("Get-Package.csv")
        if self.var2.get() == 1:
            subprocess.call(["powershell.exe", ".\Get-Item.ps1"])
            selected_options.append("Get-Item.csv")
        if self.var3.get() == 1:
            subprocess.call(["powershell.exe", ".\Get-WmiObject.ps1"])
            selected_options.append("Get-WmiObject.csv")
        if self.var4.get() == 1:
            subprocess.call(["python", ".\psutil.py"])
            selected_options.append("psutil.csv")
        self.label2.destroy()
        self.check1.destroy()
        self.check2.destroy()
        self.check3.destroy()
        self.check4.destroy()
        self.button2.destroy()
        self.label3 = tk.Label(self, text="Results:")
        self.label3.pack(pady=10)
        for option in selected_options:
            label = tk.Label(self, text=option)
            label.pack()
        self.button3 = tk.Button(self, text="Back", command=self.show_second_screen)
        self.button3.pack(pady=20)

app = Application()
app.mainloop()
    