import os
import subprocess

# Function to set ID3 tags for mp3 and flac files in a directory
def set_id3_tags(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # CHANGE THIS to your file names
            if file.endswith('.mp3') or file.endswith('.flac'):

                # Determine artist name and album name based on folder structure
                parent_folder = os.path.basename(os.path.abspath(root))
                grandparent_folder = os.path.basename(os.path.dirname(os.path.abspath(root)))
                # CHANGE THIS if your folder name is not 'Music'
                no_album = grandparent_folder == 'Music'

                artist_name = parent_folder if no_album else grandparent_folder
                album_name = '' if no_album else parent_folder

                # Song name is just the file name without the file extension
                song_name = os.path.splitext(file)[0]

                # Set ID3 tags using id3v2 command
                artist_command = f'id3v2 -a "{artist_name}" "{os.path.join(root, file)}"'
                album_command = f'id3v2 -A "{album_name}" "{os.path.join(root, file)}"'
                title_command = f'id3v2 -t "{song_name}" "{os.path.join(root, file)}"'

                # Run the id3v2 commands using subprocess
                print('FILE: ' + str(file))
                subprocess.run(artist_command, shell=True)
                print('Added Artist tag: ' + artist_name)
                if not no_album:
                    subprocess.run(album_command, shell=True)
                    print('Added Album tag: ' + album_name)
                subprocess.run(title_command, shell=True)
                print('Added Song tag: ' + song_name + '\n')

# Specify the main directory to start the search
# CHANGE THIS to your directory name
main_directory = '/Users/username/Music'

# Call the function to set ID3 tags in the specified directory
set_id3_tags(main_directory)
