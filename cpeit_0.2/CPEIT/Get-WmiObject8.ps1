# Import the necessary module
Import-Module -Name "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\Microsoft.PowerShell.Management\Microsoft.PowerShell.Management.psd1"

# Define the query to get the software inventory using Get-WmiObject
$query = "SELECT * FROM Win32_Product"

# Run the query and save the results as a JSON file encoded in UTF-8
Get-WmiObject -Query $query | Select-Object Name, Version, Vendor, InstallDate, InstallLocation | ConvertTo-Json | Out-File -Encoding utf8 -FilePath ".\Got-WmiObject.json"
