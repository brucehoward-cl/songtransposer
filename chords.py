class Chord:
    name = str()
    root = str()
    third = str()
    fifth = str()

    def __init__(self, name):
        self.name = name
        if self.name.find('min') > 0:
            print('this chord is minor')
            self.third = 'minor'
        else:
            print('this chord is major')
            self.third = 'major'

    def __str__(self):
        return f'{self.name}'

    