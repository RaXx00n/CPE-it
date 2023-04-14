import subprocess

# Run the PowerShell scripts
subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'Get-WmiObject8.ps1'])
subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'Get-Item8.ps1'])
subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'Get-Package8.ps1'])

# Run the Python script
subprocess.run(['python', 'combine_json.py'])
subprocess.run(['python', 'generate_inventory.py'])
subprocess.run(['python', 'cpe_guess.py'])
subprocess.run(['python', 'cpe_guess2.py'])