import chords
import factory

class Song:
    # chords = []   # make this immutable!
    chord_progression = []
    
    def __init__(self, chord_prog, injected_factory):
        self.chords = chord_prog
        self.chord_factory = injected_factory

        for chord_type in self.chords:
            chord = self.chord_factory.get_chord(chord_type)
            self.chord_progression.append(chord)

        self.key = self.chord_progression[0]
        print(f'song key is: {self.key}')

    def transpose(self, new_key):
        #index = notes.NOTES.index(new_key)
        for chord in self.chord_progression:
            print(f'transposing {chord} by a hardcoded # of halfsteps')
            chord.transpose(1)


