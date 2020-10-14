import factory
import song
import instructions
import re

from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#clear_screen()
#print(str(instructions.instructions))
user_song_input = input("Enter a chord progression: ")
chord_progression = re.findall(r'[\w]+\b', user_song_input)

chord_factory = factory.Factory()   
song = song.Song(chord_progression, chord_factory) #chord factory object is being injected into song

user_new_key = input("Enter a new key: ")
#new_key = re.match(r'[a-gA-G]', user_new_key)

song.transpose(user_new_key)
print(song.chord_progression)

