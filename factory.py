import chords

class Factory:
    def get_chord(self, chord_type):

        if chord_type.find('min') > 0:
            #create minor chord
            chord = chords.MinorChord(chord_type)
        else:
            chord = chords.MajorChord(chord_type)

        return chord
