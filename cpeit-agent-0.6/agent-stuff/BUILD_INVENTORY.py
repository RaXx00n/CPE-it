import subprocess

# Run the PowerShell scripts to gather the info from the registry, package manager and uninstall strings
subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'Get-WmiObject8.ps1'])
subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'Get-Item8.ps1'])
subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'Get-Package8.ps1'])

# Run the scripts to combine the json together and then make a software inventory to display in the pane
subprocess.run(['python', 'combine_json.py'])
subprocess.run(['python', 'generate_inventory.py'])