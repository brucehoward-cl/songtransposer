from notes import SCALE
import re


class IChord:
    """This class defines common methods for all Chord classes"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def convert_note(self, note, halfsteps):
        """This method locates a note in the scale, adds the number of halfsteps, and returns a new note"""
#        place_in_SCALE = [n for n in SCALE if n.startswith(note)]
        place_in_SCALE = [n for n in SCALE if n.startswith(note) or n.endswith(note)]  #one place where a single letter variable name makes sense
        new_note_index = SCALE.index(place_in_SCALE[0]) + halfsteps
        if new_note_index > 11:     #This section effectively wraps the index around the scale
            new_note_index -= 12
        elif new_note_index < 0:
            new_note_index += 12
        print(f'converting {note} \tto new note ({SCALE[new_note_index]})')
        return SCALE[new_note_index]

    def transpose(self, number_of_halfsteps):
        """This method takes an integer representing the number of halfsteps to transpose each note in the chord to"""
        self.root = self.convert_note(self.root, number_of_halfsteps)
        self.third = self.convert_note(self.third, number_of_halfsteps)
        self.fifth = self.convert_note(self.fifth, number_of_halfsteps)


class MinorChord(IChord):
    third = str()
    fifth = str()

    def __init__(self, name):
        super().__init__(name)

        self.root_shortname = re.match(r'[A-G][#b]?', name).group(0)
        self.root = [note for note in SCALE if note.startswith(self.root_shortname) or note.endswith(self.root_shortname)][0]
        self.minor = True

        index_for_third = SCALE.index(self.root) + 3
        if (index_for_third) > 11:
            index_for_third -= 12
        self.third = SCALE[index_for_third]

        index_for_fifth = SCALE.index(self.root) + 7
        if (index_for_fifth) > 11:
            index_for_fifth -= 12
        self.fifth = SCALE[index_for_fifth]
        print(f'(from Chord {self.name}); \troot: {self.root}; \tthird: {self.third}; \tfifth: {self.fifth}')

    def transpose(self, number_of_halfsteps):
        super().transpose(number_of_halfsteps)
        self.name = f'{self.root}min'


class MajorChord(IChord):
    third = str()
    fifth = str()

    def __init__(self, name):
        super().__init__(name)

        self.root_shortname = re.match(r'[A-G][#b]?', name).group(0)
        self.root = [note for note in SCALE if note.startswith(self.root_shortname) or note.endswith(self.root_shortname)][0]

        index_for_third = SCALE.index(self.root) + 4
        if (index_for_third) > 11:
            index_for_third -= 12
        self.third = SCALE[index_for_third]

        index_for_fifth = SCALE.index(self.root) + 7
        if (index_for_fifth) > 11:
            index_for_fifth -= 12
        self.fifth = SCALE[index_for_fifth]
        print(f'(from Chord {self.name}); \troot: {self.root}; \tthird: {self.third}; \tfifth: {self.fifth}')

    def transpose(self, number_of_halfsteps):
        super().transpose(number_of_halfsteps)
        self.name = f'{self.root}'


