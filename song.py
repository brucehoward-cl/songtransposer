import chords
import factory
from notes import SCALE
import re

class Song:
    def __init__(self, injected_factory):
        self.chord_factory = injected_factory
        self.chord_progression = []


    def insert_chord_progression(self, chord_prog):
        """This method takes a list of strings that represent individual chord names in the progression.
        It creates a chord object for each chord name and appends it to its chord_progression list""" 
        self.chords = chord_prog
        self.chord_progression = [] # re-initialize the chord_progression for successive uses
        for chord_type in self.chords:
            chord = self.chord_factory.get_chord(chord_type)
            self.chord_progression.append(chord)
        self.key = self.chord_progression[0].root
        print(f'song key is: {self.key}')


    def transpose(self, new_key):
        """This method takes a string that represents to what key this song needs to be transposed.
        It stores the new key as the song key, and transposes each individual chord in its chord_progression."""
        old_key_index = SCALE.index(str(self.key))

        entry_in_SCALE = [note for note in SCALE if note.startswith(new_key) or note.endswith(new_key)]
        new_key_index = SCALE.index(entry_in_SCALE[0])

        interval_change = new_key_index - old_key_index
        for chord in self.chord_progression:
            print(f'\ntransposing {chord} by {interval_change} halfsteps')
            chord.transpose(interval_change)


    @staticmethod
    def validate_progression(user_input):
        validity = True
        for each_entry in user_input:
            valid_entry = re.match(r'^[A-G]{1}[#b]?(min)?(maj)?7?', each_entry)  #this is far from perfect; Bbminmaj for example will validate; but it catches a lot
            if valid_entry.string != valid_entry.group(0):
                print(f'{each_entry} is not a valid chord name/type')
                validity = False
        return validity
            
