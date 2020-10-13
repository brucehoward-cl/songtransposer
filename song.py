import chords

class Song:
    # chords = []   # make this immutable!
    chord_progression = []
    
    
    def __init__(self, chord_prog):
        self.chords = chord_prog
        for chord in self.chords:
            chrd = chords.Chord(chord)
            self.chord_progression.append(chrd)
        self.key = self.chord_progression[0]

    def transpose(self, new_key):
        #index = notes.NOTES.index(new_key)
        for chord in self.chord_progression:
            print(f'transposing {chord} by a hardcoded # of halfsteps')
            chord.transpose(1)


