from pyo import *
from mido import MidiFile
class BasicOsc:
    def self(self, **args):
        EventInstrument.__init__(self, **args)

        # self.freq is derived from the 'degree' argument.
        self.phase = Phasor([self.freq, self.freq * 1.003])

        # self.dur is derived from the 'beat' argument.
        self.duty = Expseg([(0, 0.05), (self.dur, 0.5)], exp=4).play()

        self.osc = Compare(self.phase, self.duty, mode="<", mul=1, add=-0.5)

        # EventInstrument created the amplitude envelope as self.env.
        self.filt = ButLP(self.osc, freq=5000, mul=self.env).out()

def playfile(file, instrument):
    instrument.note = (MidiFile(file))
    for message in instrument.note.play():
        s.addMidiEvent(*message.bytes())
        s = Server().boot()

def choosekey():
    keys = input("""Choose your notes or preset separated by spaces:\n
                 C3 - 50
                 C# - 51
                 D  - 52
                 D# - 53
                 E  - 54
                 F  - 55
                 F# - 56
                 G  - 57
                 G# - 58
                 A  - 59
                 A# - 60
                 B  - 61
                 C4 - 62
                 """)
    lister = keys.split(" ")
    nl = []
    if "minor" in lister:
        nl = [50, 53, 55, 57, 60]
    if "major" in lister:
        nl = [50, 54, 55, 57, 59]
    if "phrygian" in lister:
        nl = [50, 51, 54, 55, 57, 58, 60]
    ok = False
    if len(nl) < 1:
        while ok != True:
            try:
                for ent in lister:
                    nl.append(int(ent))
            except ValueError as e:
                print("You mistyped a number or entered a non-number character.")
            ok = True
    return nl




