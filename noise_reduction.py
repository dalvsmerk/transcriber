import soundfile as sf
import noisereduce as nr
import numpy as np
import os

def read_audio(audio_path):
    # valid_path = audio_path.replace('\\', os.sep)
    
    # Reads as float64 by default
    # If reads as float32 then array is empty
    rec, sr = sf.read(audio_path, dtype='float64')

    # whisper requires float32 np.array if using np.array as input
    return np.float32(rec), sr


def reduce_noise(audio_array, sample_rate):
    # whisper transcribes better with audio cleaned using stationary algorithm
    return nr.reduce_noise(y=audio_array, sr=sample_rate, stationary=True)
