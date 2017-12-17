Title: Read event log file (evtx) with Tx (LINQ to Events)
Date: 2017-12-17 12:09
Category: C#
Tags: c#, ling, evtx, event log, tx

Example:
-------

```csharp
using System.Reactive;
using System.Reactive.Linq;
using Tx.Windows;
...
var playback = new Playback();
playback.AddLogFiles(@"C:\Application.evtx");

var allEvents = playback.GetObservable<SystemEvent>();
var fromTime = new DateTime(2017, 12, 16, 20, 0, 0);
var recentEvents =
	from ev in allEvents
	where ev.OccurenceTime >= fromTime
	select ev;

using (recentEvents.Subscribe(evt => {
	Console.WriteLine("{0}, EventID: {1}", evt.OccurenceTime, evt.Header.EventId);
}))
{
	playback.Run();
}
```

The example reads recent events from an evtx file using the Microsoft/Tx (LINQ to Events) library.

Tx library parses raw events to `SystemEvent` objects, which contain only a subset of the information in an `EventRecord`.
