Title: Using GStreamer with playbin and audio filter as internet radio player
Date: 2016-10-09 08:49
Category: Python
Tags: python, gstreamer, audio, radio, player, media, streaming, sink

Install:
--------

```bash
sudo apt-get install gstreamer1.0 gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good
```

Example:
--------

```python
#!/usr/bin/env python3
import gi
import threading
gi.require_version('Gst', '1.0')
gi.require_version('GstBase', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gst

# Initialize threads
GObject.threads_init()

# Initialize GStreamer
Gst.init(None)

# Handle song metadata
def on_tag(bus, msg):
    taglist = msg.parse_tag()
    print('%s: %s' % (taglist.nth_tag_name(0), taglist.get_string(taglist.nth_tag_name(0)).value))

# Create a custom bin element, that will serve as audio sink to
# player bin. Audio filters will be added to this sink.
audio_sink = Gst.Bin.new('audiosink')

# Create element to attenuate/amplify the signal
amplify = Gst.ElementFactory.make('audioamplify')
amplify.set_property('amplification', 0.1)
audio_sink.add(amplify)

# Create element to play the pipeline to hardware
sink = Gst.ElementFactory.make('autoaudiosink')
audio_sink.add(sink)

amplify.link(sink)
audio_sink.add_pad(Gst.GhostPad.new('sink', amplify.get_static_pad('sink')))

# Create playbin and add the custom audio sink to it
player = Gst.ElementFactory.make("playbin", "player")
player.props.audio_sink = audio_sink

# Set URI to online radio
player.set_property('uri', 'http://...')

# Start playing
player.set_state(Gst.State.PLAYING)

# Listen for metadata
bus = player.get_bus()
bus.enable_sync_message_emission()
bus.add_signal_watch()
bus.connect('message::tag', on_tag)

loop = GObject.MainLoop()
threading.Thread(target=loop.run).start()

# Let user stop player gracefully
input('Press enter to stop playing...')

# Stop loop
player.set_state(Gst.State.NULL)
loop.quit()

```
