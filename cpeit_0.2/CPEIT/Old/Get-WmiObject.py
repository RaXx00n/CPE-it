import subprocess

# Define the PowerShell command
command = 'Get-WmiObject -Query "SELECT * FROM Win32_Product" | Select-Object Name, Version, Vendor, InstallDate, InstallLocation | ConvertTo-Json | Out-File -Encoding utf8 -FilePath .\\Got-WmiObject.json'

# Run the PowerShell command
result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print('PowerShell command ran successfully')
else:
    print('Error running PowerShell command')
    print(result.stderr)
