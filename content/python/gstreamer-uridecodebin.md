Title: Using GStreamer with uridecodebin and audio filter as internet radio player
Date: 2016-10-09 08:51
Category: Python
Tags: python, gstreamer, audio, radio, player, media, streaming, uridecodebin

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
gi.require_version('Gst', '1.0')
gi.require_version('GstBase', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gst

# Initialize threads
GObject.threads_init()

# Initialize GStreamer
Gst.init(None)

class RadioPlayer:
    def __init__(self, uri):
        # Create pipeline object
        self.pipeline = Gst.Pipeline.new("onlineradio")

        # Create the `uridecodebin` element, that will connect to the
        # online radio stream and decode the audio data. Add to pipeline
        self.decode = Gst.ElementFactory.make("uridecodebin", "decode")
        self.decode.set_property('uri', uri)
        self.pipeline.add(self.decode)

        # Convert data, if needed
        self.convert = Gst.ElementFactory.make("audioconvert", "convert")
        self.pipeline.add(self.convert)

        # Resample data, if needed
        self.resample = Gst.ElementFactory.make("audioresample", "resample")
        self.pipeline.add(self.resample)

        # Create an audio filter that will attenuate the volume level
        self.amplify = Gst.ElementFactory.make("audioamplify", "amplify")
        self.amplify.set_property('amplification', 5.0)
        print('Amplifycation: ', self.amplify.props.amplification)
        self.pipeline.add(self.amplify)

        # Create the element that will play the stream
        self.sink = Gst.ElementFactory.make("autoaudiosink", "sink")
        self.pipeline.add(self.sink)

        # Setup links between elements
        self.convert.link(self.resample)
        self.resample.link(self.amplify)
        self.amplify.link(self.sink)

        # Connect `decode` to `convert` at runtime, when the decoder pad is available -
        # after the decoders starts receiving audio data and can determine the format
        self.decode.connect("pad-added", self.decode_pad_added)

    # Connect the new src pad of `decode` to sink of `convert`
    def decode_pad_added(self, element, pad):
        pad.link(self.convert.get_static_pad("sink"))
        print("Sink added.")

    # Run the main loop of the player
    def run(self):
        print("Running...")
        self.pipeline.set_state(Gst.State.PLAYING)
        GObject.MainLoop().run()

player = RadioPlayer("http://...")
player.run()

```
