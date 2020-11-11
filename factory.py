import chords


class Factory:
    """This class contains the logic to determine what kind of chord to instantiate. 
    To handle new chords in this application, you should only have to add the chord type class,
    and update the logic in this Factory class."""
    def get_chord(self, chord_type):
        """This method takes a string that represents what type of chord to create. 
            It returns an appropriate Chord object"""
        if chord_type.find('min') > 0:
            #create minor chord
            chord = chords.MinorChord(chord_type)
        else:
            #create major chord
            chord = chords.MajorChord(chord_type)

        return chord
