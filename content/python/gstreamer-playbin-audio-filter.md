Title: Using GStreamer with playbin and audio filter as internet radio player
Date: 2016-10-09 08:46
Category: Python
Tags: python, gstreamer, audio, radio, player, media, streaming, filter

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
    print('')
    print('Tags:', taglist.n_tags())
    for key in range(taglist.n_tags()):
        print('\t%s = %s' % (taglist.nth_tag_name(key), taglist.get_string(taglist.nth_tag_name(key)).value))

# Create element to attenuate/amplify the signal
amplify = Gst.ElementFactory.make('audioamplify')
amplify.set_property('amplification', 0.1)

# Create playbin and add the custom audio sink to it
player = Gst.ElementFactory.make("playbin", "player")
player.set_property('audio_filter', amplify)

# Set URI to online radio (not playlist, direct URI)
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
