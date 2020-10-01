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
chord_progression = input("Enter a chord progression: ")

test = re.findall(r'[\w]+\b', chord_progression)
song = song.Song(test)

print(song.chords)
print(song.chord_progression[0])
print(song.chord_progression[1])

