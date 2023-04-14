import tkinter as tk
from tkinterweb import HtmlFrame
import subprocess
import shutil
import os

class CPEitGUI:
    def __init__(self, master):
        self.master = master
        master.title("CPEit")
        master.attributes('-fullscreen', True)
        master.configure(bg='black')
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)

        # Create left panel
        left_panel = tk.Frame(master, bg='black', width=100)
        left_panel.grid(row=0, column=0, sticky='nsew')
        left_panel.grid_propagate(False)
        left_panel.grid_rowconfigure(0, weight=1)
        left_panel.grid_rowconfigure(1, weight=1)

        # Create button "Build Inventory"
        build_button = tk.Button(left_panel, text="Build Inventory", command=self.build_inventory, bg='black', fg='white', font=('Helvetica', 14))
        build_button.grid(row=0, column=0, sticky='nsew')

        # Create button "Export CPEs"
        export_button = tk.Button(left_panel, text="Export CPEs", command=self.export_cpes, bg='black', fg='white', font=('Helvetica', 14))
        export_button.grid(row=1, column=0, sticky='nsew')

        # Create image above the buttons
        image = tk.PhotoImage(file="image.gif")
        img_label = tk.Label(left_panel, image=image, bg='black')
        img_label.image = image
        img_label.grid(row=2, column=0, sticky='nsew')

        # Create HTML reader widget
        self.html_frame = HtmlFrame(master, horizontal_scrollbar='none')
        self.html_frame.grid(row=0, column=1, sticky='nsew')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=3)
        left_panel.grid(sticky='nsew')

    def build_inventory(self):
        subprocess.run(['python', 'ENUMERATE.py'])
        html_path = 'Software-Inventory.html'
        with open(html_path, 'r') as f:
            html_content = f.read()
        self.html_frame.load_html(html_content)

    def export_cpes(self):
        shutil.copyfile("PotentialCPE.txt", os.path.join(os.path.expanduser("~"), "Desktop", "PotentialCPE.txt"))
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop", "PotentialCPE.txt"))



root = tk.Tk()
gui = CPEitGUI(root)
root.mainloop()
