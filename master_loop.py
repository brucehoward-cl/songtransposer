import factory
import song
import instructions
import re
import notes

from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#clear_screen()



while True:
    #print(str(instructions.instructions))
    user_song_input = input("Enter a chord progression (Q to Quit): ")
    if re.search(r'Q', user_song_input, re.I):
        break;
    
    chord_progression = re.findall(r'[\w]+\b', user_song_input)

    chord_factory = factory.Factory()   
    song = song.Song(chord_progression, chord_factory) #chord factory object is being injected into song
    
    user_new_key = input("Enter a new key: ")
    new_key = re.search(r'[a-gA-G]?[#b]?', user_new_key)
    print(f'result from re.match {new_key.group(0)}')


    song.transpose(new_key.group(0))
    print(song.chord_progression)




print('Thanks for playing')