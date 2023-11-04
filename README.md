# id3-folder-tagger
A python script to add id3 album and artist tags based on folder structure.

The script will look through a music folder's structure, taking the child folder as the artist and the grandchild folder as the album.  

Requires command line tool id3v2, can be found here: https://formulae.brew.sh/formula/id3v2  
brew folmula: ```brew install id3v2```  
  
The folder structure must look like this:  
```
Music/  
    ├── artist/  
    │   ├── song.mp3  
    │   └── song.flac  
    ├── artist/  
    │   ├── album/  
    |   |   ├── song.mp3  
    |   |   └── song.flac  
    |   └── album/  
    |       ├── song.mp3  
    |       └── song.flac  
    ...  
```
If there is no album inside the artist folder the script will not add one.  

N.B. Make sure to change the script to use your music directory, your file extensions and your music folder name. Search for "CHANGE THIS" in the comments.  
