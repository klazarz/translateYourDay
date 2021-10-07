#!/usr/local/bin/ python3

import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import soundfile as sf


fs = 44100  # Sample rate
seconds = 5  # Duration of recording

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file 

# # Extract audio data and sampling rate from file 
# data, fs = sf.read('output.wav') 
# # Save as FLAC file at correct sampling rate
# sf.write('output.flac', data, fs)


r = sr.Recognizer()

mic = sr.Microphone(device_index=3)

# audio = sr.AudioFile('output.flac')
with mic as source:
    c_audio = r.record(source)

trans = r.recognize_google(c_audio)

print(trans)