'''
from flask import Flask, render_template
import os

app = Flask(__name__)

# Specify the directory where your audio files are stored
AUDIO_DIRECTORY = 'static/audio'

@app.route('/')
def index():
    audio_files = [file for file in os.listdir(AUDIO_DIRECTORY) if file.endswith('.mp3')]
    return render_template('index.html', audio_directory=AUDIO_DIRECTORY, audio_files=audio_files)

if __name__ == '__main__':
    app.run(debug=True)
'''

from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# Specify the directory where your audio files are stored
AUDIO_DIRECTORY = 'static/audio'

# Get a list of all audio files in the specified directory
audio_files = [file for file in os.listdir(AUDIO_DIRECTORY) if file.endswith('.mp3')]

# Shuffle the audio files for the initial playlist
random.shuffle(audio_files)

# Index to keep track of the current playing song
current_index = 0


@app.route('/')
def index():
    global current_index
    current_song = audio_files[current_index]
    return render_template('index.html', audio_directory=AUDIO_DIRECTORY, audio_files=audio_files, current_index=current_index)


@app.route('/play_song/<int:selected_index>')
def play_song(selected_index):
    global current_index
    current_index = selected_index
    return {'status': 'success'}


@app.route('/play_next')
def play_next():
    global current_index
    current_index = (current_index + 1) % len(audio_files)
    return {'status': 'success'}


@app.route('/play_previous')
def play_previous():
    global current_index
    current_index = (current_index - 1) % len(audio_files)
    return {'status': 'success'}


@app.route('/shuffle_playlist')
def shuffle_playlist():
    global current_index
    random.shuffle(audio_files)
    # Reset the current_index to 0 after shuffling
    current_index = 0
    return {'status': 'success'}


if __name__ == '__main__':
    app.run(debug=True)

