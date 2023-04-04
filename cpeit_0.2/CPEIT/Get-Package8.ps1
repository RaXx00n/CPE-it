$packages = Get-Package | Select-Object Name, Version, ProviderName
$packages | ConvertTo-Json | Out-File -Encoding UTF8 -FilePath 'Got-Package.json'
