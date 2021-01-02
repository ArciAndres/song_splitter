# -*- coding: utf-8 -*-

import numpy as np
import os
from pathlib import Path
#%%

cwd = Path('./') # Current working directory

song_name = 'Die Ärzte - Westerland'

lyrics_path = cwd / 'lyrics' / (song_name+'.txt')
song_path = cwd / 'songs' / (song_name+'.mp3')
#%%

assert os.path.exists(lyrics_path) , "Please add a text file with the lyrics with the name " + song_name + ".txt"
assert os.path.exists(song_path) , "Please add an .mp3 file of the song with the name " + song_name + ".mp3"

#%%


song_name

