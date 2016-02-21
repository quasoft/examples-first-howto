Title: Remove empty lines with PowerShell
Date: 2016-02-21 10:11
Category: PowerShell
Tags: powershell, unique, windows

Examples:
---------

Full version:

```powershell
Get-Content input.txt | Where-Object {$_ -ne ""} > output.txt
```

Short version:

```powershell
cat input.txt | ? {$_ -ne ""} > output.txt
```
