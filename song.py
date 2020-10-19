import chords
import factory
import notes

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
        old_key_index = notes.NOTES.index(str(self.key))

#        new_key_index = notes.NOTES.index(new_key)
        value_in_NOTES = [e for e in notes.NOTES if e.startswith(new_key)]
        new_key_index = notes.NOTES.index(value_in_NOTES[0])

        interval_change = new_key_index - old_key_index
        for chord in self.chord_progression:
            print(f'transposing {chord} by {interval_change} halfsteps')
            chord.transpose(interval_change)


