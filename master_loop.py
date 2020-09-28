import song
import chords
import modes
import notes
import instructions
from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear_screen()
print(str(instructions.instructions))
chord_progression = input("Enter a chord progression: ")

print(chord_progression)


