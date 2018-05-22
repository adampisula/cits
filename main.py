import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 2.5   # in seconds, may be float
f = 130.81        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples1 = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()
samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*(f*2)/fs)).astype(np.float32).tobytes()
samples3 = (np.sin(2*np.pi*np.arange(fs*duration)*(f*4)/fs)).astype(np.float32).tobytes()

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
#stream.write(volume*samples)
stream.write(samples1)
stream.write(samples2)
stream.write(samples3)

stream.stop_stream()
stream.close()

p.terminate()


