import tkinter as tk
import os
import datetime
import subprocess

def run_script(script_path):
    os.system(f'powershell.exe -ExecutionPolicy RemoteSigned -File "{script_path}"')

def combine_json():
    print("Processing - Combining JSON files")
    subprocess.run(["python", "combine_json.py"], capture_output=True, text=True)

def convert_json():
    print("Processing - Combining JSON files")
    subprocess.run(["python", "json2ndjson.py"], capture_output=True, text=True)

def cpe_guess():
    print("Generating potential CPEs...")
    subprocess.run(["python", "cpe_guess.py"], capture_output=True, text=True)
    subprocess.run(["python", "cpe_guess2.py"], capture_output=True, text=True)
    print("Potential CPEs generated.")

def generate_inventory():
    print("Generating inventory...")
    subprocess.run(["python", "generate_inventory.py"], capture_output=True, text=True)
    subprocess.run(["python", "generate_inventory_with_guess.py"], capture_output=True, text=True)
    print("Inventory generated.")

def view_inventory():
    print("Viewing inventory...")
    os.startfile("Software-Inventory.html")

def build_inventory():
    if registry_check.get() == 1:
        print("Building inventory from Registry Tree (HKLM)...")
        run_script('Get-Item8.ps1')
        print("Inventory from Registry Tree (HKLM) built.")

    if wmi_check.get() == 1:
        print("Building inventory from Windows Management Instrumentation...")
        run_script('Get-WMIobject8.ps1')
        print("Inventory from Windows Management Instrumentation built.")

    if package_check.get() == 1:
        print("Building inventory from PackageManagement...")
        run_script('Get-Package8.ps1')
        print("Inventory from PackageManagement built.")

    combine_json()
    convert_json()
    cpe_guess()
    generate_inventory()

# Create the main window
root = tk.Tk()
root.title("Software Inventory Builder")

# Create the left frame for buttons
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create the right frame for output
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the welcome label
welcome_label = tk.Label(left_frame, text="Welcome to the Software Inventory Builder!")
welcome_label.pack(pady=10)

# Create the check boxes
registry_check = tk.IntVar()
wmi_check = tk.IntVar()
package_check = tk.IntVar()

registry_checkbox = tk.Checkbutton(left_frame, text="Registry Tree (HKLM)", variable=registry_check)
wmi_checkbox = tk.Checkbutton(left_frame, text="Windows Management Instrumentation", variable=wmi_check)
package_checkbox = tk.Checkbutton(left_frame, text="PackageManagement", variable=package_check)

registry_checkbox.pack()
wmi_checkbox.pack()
package_checkbox.pack()

# Create the Build Inventory button
build_button = tk.Button(left_frame, text="Build Inventory", command=build_inventory)
build_button.pack(pady=10)

# Create the View Inventory button
view_button = tk.Button(left_frame, text="View Inventory", command=view_inventory)
view_button.pack(pady=10)

# Create the output text widget
output_text = tk.Text(right_frame, height=20, width=80)
output_text.pack()

# Redirect stdout to the output text widget
import sys
class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)

sys.stdout = StdoutRedirector(output_text)

# Start the main loop
root.mainloop()
