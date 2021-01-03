# Song splitter
A small manual script to cut and save sentences from an song (or any audio file). It was built to load pieces of audio to language learning tools, in my case [Memrise](https://www.memrise.com/), and match with the lyrics.

Nothing really fancy, but could be much more improved with an automated cutting method getting the exact time stamps from lyrics services like Musixmatch or other karaoke softwares. 

## Operation

### Create Song Chunks

Steps:

0. (Only once)

   `git clone git@github.com:ArciAndres/song_splitter.git`

   `cd song_splitter`

1. Create a folder of the desired song in the `songs` folder. 

   The suggestion of the convention is: `Author - name_of_the_song`, but it is optional. 

2. Get an .mp3 file from the desired song and put in the the created folder with the name `song.mp3`. 

   Easy way (works on 02/01/2021): https://freemp3cloud.com/

3. Get the full lyrics of the song, save in a text file and name it `lyrics.txt`.

   By now, the structure of the folder should see like this:

   ```
   ​```
   song_splitter
   │   README.md
   │   file001.txt    
   │
   └───songs
   │   │   Author_name-song
   │   │   |	song.mp3
   |	|	|	lyrics.txt
   ​```
   ```

   

4. Load the files to Memrise. Does not take long, but must be done manually :(. (Someone could contribute with an desktop automation script to do this).

   ![MemriseFileLoad](D:\GoogleDrive\MasterTemp\song_cutter_GIT\readme\MemriseFileLoad.png)

   

## Troubleshooting

* If `pydub` presents problems, make sure you have `ffmpeg` installed. The package can be installed with `conda` as:

  `conda install -c conda-forge ffmpeg`

