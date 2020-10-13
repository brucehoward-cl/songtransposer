import notes

class Chord:
    name = str()
    root = str()
    third = str()
    fifth = str()

    def __init__(self, name):
        self.name = name
        self.root = name[0]
        if self.name.find('min') > 0:
            index_for_third = notes.NOTES.index(self.root) + 3
            if (index_for_third) > 11:
                index_for_third -= 12
            self.third = notes.NOTES[index_for_third]
        else:
            index_for_third = notes.NOTES.index(self.root) + 4
            if (index_for_third) > 11:
                index_for_third -= 12
            self.third = notes.NOTES[index_for_third]
        index_for_fifth = notes.NOTES.index(self.root) + 7
        if (index_for_fifth) > 11:
            index_for_fifth -= 12
        self.fifth = notes.NOTES[index_for_fifth]
        print(f'(from Chord); root: {self.root}; third: {self.third}; fifth: {self.fifth}')

    def __str__(self):
        return f'{self.name}'

    def convert_note(self, note, halfsteps):
        new_note_index = notes.NOTES.index(note) + halfsteps
        if new_note_index > 11:
            new_note_index -= 12
        elif new_note_index < 0:
            new_note_index += 12
        print(f'converting {note} to new index ({new_note_index}: {notes.NOTES[new_note_index]})')
        return notes.NOTES[new_note_index]


    def transpose(self, number_of_halfsteps):
        self.root = self.convert_note(self.root, number_of_halfsteps)
        self.third = self.convert_note(self.third, number_of_halfsteps)
        self.fifth = self.convert_note(self.fifth, number_of_halfsteps)

