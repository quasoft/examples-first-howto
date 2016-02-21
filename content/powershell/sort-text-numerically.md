Title: Sort text numerically with PowerShell
Date: 2016-02-21 09:58
Category: PowerShell
Tags: powershell, sort, windows

Examples:
---------

Full version:

```powershell
Get-Content input.txt | For-Each { [Int] $_ } | Sort-Object > output.txt
```

Short version with aliases:

```powershell
cat input.txt | % { [Int] $_ } | sort > output.txt
```

Sample input file (`input.txt`):

	10
	1
	1000
	100
	9
	900
	9000

Sample output file (`output.txt`):

	1
	9
	10
	100
	900
	1000
	9000

Explanation
-----------

The command above sorts the contents of the input file as numbers.

First, `Get-Content` command reads the contents of the text file.

Content is passed to `For-Each` command, which casts each line to integer, thus converting the text to number.

Then, the list of numbers is passed to `Sort-Object` command, which sorts numbers in ascending order.

Finally, result is saved to output text file.

If the text file contains unwanted duplicate values, those can be removed from result by adding the `Get-Unique` as the last command in the pipeline:

```powershell
Get-Content input.txt | For-Each { [Int] $_ } | Sort-Object | Get-Unique > output.txt
```
