Title: Read XML file with namespaces in C#
Date: 2016-02-27 21:06
Category: C#
Tags: c#, ling, xml, namespace

Example:
-------

```csharp
using System.Xml.Linq;
...
var XNamespace ns = "http://www.somedomain.com/Application/Options";

var options = XDocument.Load(@"NamespacedOptions.xml")
    .Root
    .Element(ns + "OptionList")
    .Elements(ns + "Option")
    .Select(o => new {
        Key = (string)o.Attribute("Name"),
        Value = (string)o.Attribute("Value")
    })
    .ToDictionary(
        o => o.Key,
        o => o.Value
    );
```

The code in the example reads options from namespaced root element `Application` into a dictionary object.

```xml
<?xml version="1.0" encoding="utf-8"?>
<Application xmlns="http://www.somedomain.com/Application/Options">
  <OptionList>
    <Option Name="ConnectTimeout" Value="5" />
    <Option Name="RetryCount" Value="3" />
  </OptionList>
</Application>
```
