Title: Create sinusoid signal and store to wave file
Date: 2016-01-10 22:50
Category: Python/NumPy
Tags: python, numpy, dsp

Examples:
---------

### Create sinusoid signal and store to wave file

```python
import numpy as np
import pylab as plot
import wave

sample_rate = 44100
frequency = 1000
duration = 5
bits = 16
samples = duration * sample_rate
max_amp = 2**(bits - 1) - 1

# Synthesize sinusoidal signal
t = np.arange(samples) / float(sample_rate)
signal = np.sin(2 * np.pi * frequency * t) * max_amp

# Convert sample values from float to signed integer
signal = signal.astype(np.int16)

# Limit amplitude to maximum of 16 bits - 32767
signal.clip(-max_amp, max_amp)

# Write signal to wave file Mono, 16 bit, 44100 Hz
wav = wave.open(r'test.wav', 'w')
wav.setnchannels(1)
wav.setsampwidth(2)
wav.setframerate(sample_rate)
wav.writeframes(signal)

# Plot first 1000 samples
signal = signal[0:1000]
t = t[0:1000]

plot.plot(t, signal)
plot.grid()
plot.xlabel('samples')
plot.ylabel('amplitude')
plot.show()
```

![Plot of sinusoid]({filename}/images/numpy-synthetize-sinusoid.gif)
