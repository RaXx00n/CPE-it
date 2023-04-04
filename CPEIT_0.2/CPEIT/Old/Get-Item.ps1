# Retrieve software inventory
$items = Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |
        Select-Object DisplayName, DisplayVersion, Publisher, InstallDate, InstallLocation, UninstallString

# Convert to JSON and save to file
$items | ConvertTo-Json | Out-File Got-Item.json
