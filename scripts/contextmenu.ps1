New-Item -Path "HKCU:\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" -Name "InprocServer32" -force -value ""
taskkill /f /im explorer.exe
Start-Sleep -Seconds 1.5
Start-Process explorer.exe