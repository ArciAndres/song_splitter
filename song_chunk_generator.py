import os
from pathlib import Path
import pydub 
import re
from time import time, sleep
import pandas as pd
import argparse
from pygame import mixer


__version__ = '0.2.0'
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
    parser.add_argument('--song_chunks', '-sc', default=False, action='store_true')
    parser.add_argument('--timestamps', '-ts', default=False, action='store_true')
    
    return parser

#%%

def song_chunk_generator(args):    
    cwd = Path('./') # Current working directory
    
    song_name = args.song_name
    
    song_folder = cwd / 'songs' / song_name
    song_path = song_folder / 'song.mp3'
    export_folder = song_folder / 'export'
    
    ts_file = (export_folder / 'timestamps.csv')
    assert ts_file.exists(), "You must create the timestamps before generating the chunks."
    
    df = pd.read_csv(ts_file, sep='_', encoding='utf-8-sig')
    timestamps = df.T.to_dict().values()
    
    ## Generate audio chunks from timestapms
    song = pydub.AudioSegment.from_mp3(str(song_path))
    
    for ts in timestamps:
        ## Trims the audio piece in the indicated interval (in milliseconds)
        newAudio = song[(ts['t0']-0.3)*1000:(ts['t1']+0.3)*1000]
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
    
    song_folder = cwd / 'songs' / song_name
    
    song_path = song_folder / 'song.mp3'
    lyrics_path = song_folder / 'lyrics.txt'
    export_folder = song_folder / 'export'
    
    assert os.path.exists(lyrics_path) , ("Please add a text (lyrics.txt) to the folder " / song_folder)
    assert os.path.exists(song_path) , ("Please add an audio file (song.mp3) to the folder " / song_folder)
    if not song_folder.exists():
        export_folder.mkdir()
    
    ## Read lyrics file
    with open(lyrics_path, 'r', encoding='utf-8') as f:
        lyrics = f.read().splitlines()

    timestamps = []
    
    ## Intro
    
    print(">>> Start playing the song in ", end='')
    
    for i in range(args.wait_time,0, -1):
        print("%d, " %i, end=''); sleep(1)
    print("\nMUSIC ON!!")
    
    mixer.init()
    mixer.music.load(str(song_path)) # you may use .mp3 but support is limited
    mixer.music.play()

    start = time()
    
    # Start the timestamp sequence. Pay special attention. 
    for i, sentence in enumerate(lyrics):
        
        timestamp = {'i': i , 'sentence': sentence}
        
        print('\n> ', sentence)
        print('> ', '[ _ , _ ]')
      
        if input().startswith('x'): break        
        t = time() - start
        timestamp['t0'] = t
        print('> ', sentence)
        print('> ', '[ {:.3f}'.format(timestamp['t0']), ', _ ]')
    
        if input().startswith('x'): break
        t = time() - start
        timestamp['t1'] = t
        print('> ', sentence)
        print('> ', '[ {:.3f}'.format(timestamp['t0']), ', {:.3f} ]'.format(timestamp['t1']))   
    
        timestamps.append(timestamp)
        
    mixer.music.stop()
    df = pd.DataFrame(timestamps)
    export_file = export_folder / 'timestamps.csv'
    df.to_csv(export_file, sep='_', encoding='utf-8-sig')
    print("==== End of lyrics =====")
    print(">> Timestamps saved successfully in ", (export_file))
        
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
args.song_name = "AnnenMayKantereit - Freitagabend"

cwd = Path('./') # Current working directory

song_name = args.song_name
song_path = cwd / 'songs' / (song_name+'.mp3')
export_folder = cwd / 'export' / (song_name)

#%%
timestamps_generator(args)
#%%
from pdb import set_trace
#set_trace()
song_chunk_generator(args)