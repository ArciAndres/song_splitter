from pathlib import Path
import json
import pydub 
import re

#%%

cwd = Path('./') # Current working directory

song_name = 'Die Ärzte - Westerland'

lyrics_path = cwd / 'lyrics' / (song_name+'.txt')
song_path = cwd / 'songs' / (song_name+'.mp3')
export_folder = cwd / 'export' / (song_name)

with open(export_folder / 'timestamps.json') as f:
    timestamps = json.load(f)
#%%

for timestamp in timestamps:
    timestamp['t0'] = timestamp['t0']-0.2


#%%

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
