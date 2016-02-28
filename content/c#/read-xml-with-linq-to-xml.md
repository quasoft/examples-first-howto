Title: Read XML file with LINQ to XML in C#
Date: 2016-02-27 20:23
Category: C#
Tags: c#, ling, xml

Example:
-------

```csharp
using System.Xml.Linq;
...
var options = XDocument.Load(@"Options.xml")
    .Root
    .Element("OptionList")
    .Elements("Option")
    .Select(o => new {
        Key = (string)o.Attribute("Name"),
        Value = (string)o.Attribute("Value")
    })
    .ToDictionary(
        o => o.Key,
        o => o.Value
    );
```

The snippet above reads options from a XML file (`Options.xml`) into a dictionary object:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Application>
  <OptionList>
    <Option Name="ConnectTimeout" Value="5" />
    <Option Name="RetryCount" Value="3" />
  </OptionList>
</Application>
```
