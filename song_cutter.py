# -*- coding: utf-8 -*-

import numpy as np
import os
from pathlib import Path
from time import time, sleep
import pandas as pd
import json

#%%

cwd = Path('./') # Current working directory

song_name = 'Die Ärzte - Westerland'

lyrics_path = cwd / 'lyrics' / (song_name+'.txt')
song_path = cwd / 'songs' / (song_name+'.mp3')
export_folder = cwd / 'export' / (song_name)
#%%

assert os.path.exists(lyrics_path) , "Please add a text file with the lyrics with the name " + song_name + ".txt"
assert os.path.exists(song_path) , "Please add an .mp3 file of the song with the name " + song_name + ".mp3"
if not export_folder.exists():
    export_folder.mkdir()
#%%

## Read lyrics file

with open(lyrics_path, 'r', encoding='utf-8') as f:
    lyrics = f.read().splitlines()
    

#%%
timestamps = []

# ## Intro
# print(">>> Start playing the song in ", end='')
# print("4, ", end=''); sleep(1)
# print("3, ", end=''); sleep(1)
# print("2, ", end=''); sleep(1)
# print("1, ", end=''); sleep(1)
# print("GO!")

# start = time()
# for i, sentence in enumerate(lyrics):
    
#     timestamp = {'i': i , 'sentence': sentence}
    
#     print('\n> ', sentence, '[ _ , _ ]')
  
#     if input().startswith('x'): break        
#     t = time() - start
#     timestamp['t0'] = t
#     print('> ', sentence, '[ {:.3f}'.format(timestamp['t0']), ', _ ]')

#     if input().startswith('x'): break
#     t = time() - start
#     timestamp['t1'] = t
#     print('> ', sentence, '[ {:.3f}'.format(timestamp['t0']), ', {:.3f} ]'.format(timestamp['t1']))   

#     timestamps.append(timestamp)
    
    
#%%

# df = pd.DataFrame(timestamps)

#%%

# with open(export_folder / 'timestamps.json', 'w') as f:
#     json.dump(timestamps, f)

#%%
with open(export_folder / 'timestamps.json') as f:
    timestamps = json.load(f)

#%%

import pydub 
import numpy as np

def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")
# #%%

# song = read(song_path)

# pydub.AudioSegment.from_mp3(str(song_path))
#%%

import os
import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd
import librosa
import pandas as pd

def print_plot_play(x, Fs, text=''):
    """1. Prints information about an audio singal, 2. plots the waveform, and 3. Creates player
    
    Notebook: C1/B_PythonAudio.ipynb
    
    Args: 
        x: Input signal
        Fs: Sampling rate of x    
        text: Text to print
    """
    print('%s Fs = %d, x.shape = %s, x.dtype = %s' % (text, Fs, x.shape, x.dtype))
    plt.figure(figsize=(8, 2))
    plt.plot(x, color='gray')
    plt.xlim([0, x.shape[0]])
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
    ipd.display(ipd.Audio(data=x, rate=Fs))
# Read mp3
x, Fs = librosa.load(song_path, sr=None)
