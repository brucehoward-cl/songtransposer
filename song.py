import chords

class Song:
    # chords = []   # make this immutable!
    chord_progression = []
    
    def __init__(self, chord_prog):
        self.chords = chord_prog
        for chord in self.chords:
            chrd = chords.Chord(chord)
            self.chord_progression.append(chrd)



    def transpose(self):
        pass


