Title: Apply windowing to event log using Rx (Reactive) and Tx (LINQ to Events)
Date: 2017-12-17 12:23
Category: C#
Tags: c#, evtx, event log, rx, reactive, tx, linq

Example:
-------

```csharp
using System.Reactive;
using System.Reactive.Linq;
using Tx.Windows;
...
var playback = new Playback();
playback.AddLogFiles(@"C:\Application.evtx");
playback.StartTime = new DateTime(2017, 12, 16, 20, 0, 0);
var allEvents = playback.GetObservable<SystemEvent>();

var countValues =
	from window in allEvents.Window(TimeSpan.FromMinutes(5), playback.Scheduler)
	from cnt in window.Count()
	select cnt;

var withTime = countValues.Timestamp(playback.Scheduler);

using (withTime.Subscribe(ts => {
	Console.WriteLine("{0} {1}", ts.Timestamp, ts.Value);
}))
{
	playback.Run();
}
```

The example counts the number of events in windows of 5 minutes.

Microsoft/Tx (LINQ to Events) library is used for reading the evtx file.

`System.Reactive` is used to group the events in windows of 5 minutes.

`Playback`'s scheduler is used to create a virtual time for the events,
which matches the time at which events occured. This allows the window
function to group the events by `OccurenceTime` (the time when the event
actually happened) instead of by real time (the time the event was read from disk).