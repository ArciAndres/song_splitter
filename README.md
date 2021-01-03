# Song splitter
A small manual script to cut and generate audio chunks from an song (or any audio file). It was built to load pieces of audio to language learning tools, in my case [Memrise](https://www.memrise.com/), and match with the lyrics.

Nothing really fancy, but could be much more improved with an automated cutting method getting the exact time stamps from lyrics services like Musixmatch or other karaoke softwares. 

### Installation

It requires Python 3.x , `pygame` and `pydub` libraries.

```
git clone git@github.com:ArciAndres/song_splitter.git
cd song_splitter
pip install -r requirements.txt
```

## Create Song Chunks

   #### Create folder structure

1. Create a folder of the desired song in the `songs` folder. 

   The suggestion of the convention is: `Author - name_of_the_song`, but it is optional. 

2. Get an .mp3 file from the desired song and put in the the created folder with the name `song.mp3`. 

   Easy way (works on 02/01/2021): https://freemp3cloud.com/

3. Get the full lyrics of the song, save in a text file and name it `lyrics.txt`. It is better if it has no blank lines in between. If loading data to Memrise, preferably to match the sentence separation with the data is going to be uploaded, so no post-processing should be made. 

   By now, the structure of the folder should see like this:

   ```
   ​```
   song_splitter
   │   README.md
   |	requirements.txt
   │   song_chunk_generator.py
   │
   └───songs
   │   │   Author - name_of_the_song
   │   │   |	song.mp3
   |	|	|	lyrics.txt
   ​```
   ```
   
   #### Create timestamps
   
   Open a command console and execute:
   
   `python song_chunk_generator.py --song_name name_of_created_folder --timestamps`
   
   This will start the execution of the sequence that lets you create the timestamps to generate, playing the song on the background while shows you the lyrics. At this point, you (the user) must press `Enter` key before a sentence starts, and right before it ends, and try to make it as well as possible (no automatic timestamping yet :( ).
   
   ````
   Start playing the song in 5, 4, 3, 2, 1, 
   MUSIC ON!!
   
   >  First sentence of the song 
   >  [ _ , _ ] (Here you press enter to stamp the beggining)
   
   
   >  Freitagabend
   >  [ 12.054 , _ ] (Here you press enter to stamp the end)
   
   
   >  Second sentence of the song 
   >  [ 12.054 , 13.040 ]
   ...
   ````
   
   At the end of the process, if done correctly, it should generate a `CSV` file inside the folder `songs/song_name/export` called `timestamps.csv`, which you can modify manually to correct some miss timing during the process. 
   
   #### Generate song chunks
   
   (This can be executed automatically right after the timestamping process just by adding the `--song_chunk` tag to the command line.)
   
   Once you the timestamping process has finished you can execute the command to generate pieces of audio based on the time registered in the file `timestamps.csv`.
   
   `python song_chunk_generator.py --song_name name_of_created_folder --song_chunk`
   
   Once it is finished, you are done! You can check the `.mp3` files on the `export` folder of your song.
## Load data to Memrise 

For this example, I will add a song in German with English translations. 

1. Create a course

   If you have not do it before, you can organize your lists in levels of a course, where every rig of it would be a sentence of your song.

2. Add a level with the name of your song. 

3. Organize your sentences and translations in an Excel file, so each of the sentence corresponds to its translation, so it is easier to add to Memrise.

   In Excel, copy the two columns together (original and translation), and then click on "Bulk add words".

   ![AddWords](readme\\AddWords.png)

   ![AddToMemrise](readme\\AddToMemrise.png)

   Memrise automatically deletes any repeated sentence on the list.

4. Add the audio chunks to the corresponding sentence. The process does not take long, but must be done manually :(. (I'd be glad and thankful to see a contribution automating this).

   At this step you can ignore parts you prefer not to upload, and choose the best audio part to connect. 

![MemriseFileLoad](readme\\MemriseFileLoad.png)

5. Save the list, and start learning :D.

## Troubleshooting

* If `pydub` presents problems, make sure you have `ffmpeg` installed. The package can be installed with `conda` as:

  `conda install -c conda-forge ffmpeg`

