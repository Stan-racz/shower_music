> # **Shower Music - RASPBERRY PI**

Music playing from CLI with song upload interface

## **Used Technologies**

- Python 3
  - Flask
  - vlc-python
  - werkzeug.utils
- Bash

## **Usage**
Precise a path to the music library in the file musicPath.txt. <br>
Run the batch file named ```start.bat``` which will start the music player as well as the web server song uploading interface.
### **Available commands:**
- ```play``` : Asks the user to enter a name song then plays it.
- ```pause```: Pause/Unpause a playing song.
- ```stop``` : Stop the current playing song.
- ```random``` : Plays a random song from the library folder.
- ```quit``` : Stops the music player.
