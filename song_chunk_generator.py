import os
from pathlib import Path
import json
import pydub 
import re
from time import time, sleep
import pandas as pd
import argparse

__version__ = '0.1.0'
__author__ = u'Andrés Arciniegas'

#%%

def get_parser():
    """
    Gets the parameters of the script to execute
    """
    parser = argparse.ArgumentParser('SongChunkGenerator')
    
    version = '%(prog)s ' + __version__

    parser.add_argument('--version', '-v', action='version', version=version)


#%%

def song_chunk_generator(song_name):    
    cwd = Path('./') # Current working directory
    
    song_name = 'Die Ärzte - Westerland'
    
    song_path = cwd / 'songs' / (song_name+'.mp3')
    export_folder = cwd / 'export' / (song_name)
    
    with open(export_folder / 'timestamps.json') as f:
        timestamps = json.load(f)
    
    ## Generate audio chunks from timestapms
    
    song = pydub.AudioSegment.from_mp3(str(song_path))
    
    for ts in timestamps:
        ## Trims the audio piece in the indicated interval (in milliseconds)
        newAudio = song[ts['t0']*1000:ts['t1']*1000]
        audio_name = "%d. %s.mp3" %(ts['i'], ts['sentence'])    
        # Remove illegal path characters
        audio_name = re.sub('[^\w\-_\. ]', '', audio_name) 
    
        #Exports to an .mp3 file in the current path.
        newAudio.export( str(export_folder / audio_name), format="mp3") 
        print("> Exported: %d/%d" % (ts['i'], len(timestamps)-1))
        
#%%
def timestamps_generator():
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
    
    ## Intro
    print(">>> Start playing the song in ", end='')
    print("4, ", end=''); sleep(1)
    print("3, ", end=''); sleep(1)
    print("2, ", end=''); sleep(1)
    print("1, ", end=''); sleep(1)
    print("GO!")
    
    start = time()
    for i, sentence in enumerate(lyrics):
        
        timestamp = {'i': i , 'sentence': sentence}
        
        print('\n> ', sentence, '[ _ , _ ]')
      
        if input().startswith('x'): break        
        t = time() - start
        timestamp['t0'] = t
        print('> ', sentence, '[ {:.3f}'.format(timestamp['t0']), ', _ ]')
    
        if input().startswith('x'): break
        t = time() - start
        timestamp['t1'] = t
        print('> ', sentence, '[ {:.3f}'.format(timestamp['t0']), ', {:.3f} ]'.format(timestamp['t1']))   
    
        timestamps.append(timestamp)
    #%%
    with open(export_folder / 'timestamps.json', 'w') as f:
        json.dump(timestamps, f)
        
def main(args=None):
    
    
if __name__ == "__main__":
    
    