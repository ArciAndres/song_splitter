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
    parser.add_argument('--song_name', type=str, help='Name of the song to be processed. Audio and lyrics file have to match this name.')
    parser.add_argument('--wait_time', type=int, default=5, help='Number of seconds to wait for the user to play the song.')
    parser.add_argument('--song_chunks', default=False, action='store_true')
    parser.add_argument('--generate_timestamps', default=False, action='store_true')
    
    return parser

#%%

def song_chunk_generator(args):    
    cwd = Path('./') # Current working directory
    
    song_name = args.song_name
    song_path = cwd / 'songs' / (song_name+'.mp3')
    export_folder = cwd / 'export' / (song_name)
    
    assert (export_folder / 'timestamps.json').exists(), "You must create the timestamps before generating the chunks."
    
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
    print("====== Export completed. =======")
        
#%%
def timestamps_generator(args):
    cwd = Path('./') # Current working directory
    
    song_name = args.song_name
    
    lyrics_path = cwd / 'lyrics' / (song_name+'.txt')
    song_path = cwd / 'songs' / (song_name+'.mp3')
    export_folder = cwd / 'export' / (song_name)
    
    assert os.path.exists(lyrics_path) , "Please add a text file with the lyrics with the name " + song_name + ".txt to the folder 'lyrics'"
    assert os.path.exists(song_path) , "Please add an .mp3 file of the song with the name " + song_name + ".mp3 to the folder 'songs'"
    if not export_folder.exists():
        export_folder.mkdir()
    
    ## Read lyrics file
    with open(lyrics_path, 'r', encoding='utf-8') as f:
        lyrics = f.read().splitlines()

    timestamps = []
    
    ## Intro
    
    print(">>> Start playing the song in ", end='')
    
    for i in range(args.waiting_time+1,1, -1):
        print("%d, " %i, end=''); sleep(1)
    print("PLAY THE SONG! GO!")
    
    start = time()
    
    # Start the timestamp sequence. Pay special attention. 
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

    with open(export_folder / 'timestamps.json', 'w') as f:
        json.dump(timestamps, f)
        
#%%    
def main(args=None):
    parser = get_parser()
    args = parser.parse_args(args)
    
    if args.generate_timestamps:
        timestamps_generator(args)
    
    if args.song_chunks:
        song_chunk_generator(args)
    
if __name__ == "__main__":
    main()
#%%
#Test 

parser = get_parser()
args = parser.parse_args("")
args.song_name = "Mark Foster - Chöre"

cwd = Path('./') # Current working directory

song_name = args.song_name
song_path = cwd / 'songs' / (song_name+'.mp3')
export_folder = cwd / 'export' / (song_name)
#%%
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3(str(song_path))
play(song)
