import factory
from song import Song
import instructions
import re

from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


chord_factory = factory.Factory()   
song = Song(chord_factory) #chord factory object is being injected into song

clear_screen()
print(str(instructions.instructions))

while True:
    user_song_input = input("\nEnter a chord progression (Q to Quit; I for instructions): ")
    if re.search(r'Q', user_song_input, re.I):
        break

    if re.match(r'\s*I', user_song_input, re.I):
        clear_screen()
        print(str(instructions.instructions))
        continue

    chord_progression = re.findall(r'[\w]+\b', user_song_input)

    song.insert_chord_progression(chord_progression) 
    
    user_new_key = input("\nEnter a new key: ")
    new_key = re.search(r'[a-gA-G]?[#b]?', user_new_key)


    song.transpose(new_key.group(0))
    print('\n\n***Transposed chord progression:')
    print([chord.name for chord in song.chord_progression]) #using a list comprehension




print('Thanks for playing')