# Song splitter
A small manual script to cut and save sentences from an song (or any audio file). It was built to load pieces of audio to language learning tools, in my case [Memrise](https://www.memrise.com/), and match with the lyrics.

Nothing really fancy, but could be much more improved with an automated cutting method getting the exact time stamps from lyrics services like Musixmatch or other karaoke softwares. 

## Operation

Steps:

1. Get an .mp3 file from the desired song. 

   Easy way (works on 02/01/2021): https://freemp3cloud.com/

2. Get the full lyrics of the song.

3. 

4. Load the files to Memrise. Does not take long, but must be done manually :(. (Someone could contribute with an desktop automation script to do this).

   ![MemriseFileLoad](D:\GoogleDrive\MasterTemp\song_cutter_GIT\readme\MemriseFileLoad.png)

   

## Troubleshooting

* If `pydub` presents problems, make sure you have `ffmpeg` installed. The package can be installed with `conda` as:

  `conda install -c conda-forge ffmpeg`

