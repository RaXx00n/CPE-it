# Retrieve software inventory
$items = Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |
        Select-Object DisplayName, DisplayVersion, Publisher, InstallDate, InstallLocation, UninstallString

# Convert to JSON and save to file with UTF-8 encoding
$items | ConvertTo-Json | Out-File -Encoding utf8 Got-Item.json