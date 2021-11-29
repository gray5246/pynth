if __name__ == "__main__":
    from pyo import *
    from random import random
    from mido import MidiFile
    class Synth:
        def __init__(self, transpo=1, mul=1):
            self.transpo = Sig(transpo)
            self.note = Notein(poly=10, scale=1, first=0, last=127)

            self.pit = self.note["pitch"] * self.transpo
            self.amp = MidiAdsr(self.note["velocity"], attack=0.001, decay=0.05, sustain=0.7, release=0.5, mul=0.1, )

            self.osc1 = LFO(self.pit, sharp=0.5, type=2, mul=self.amp).mix(1)
            self.osc2 = LFO(self.pit * 0.997, sharp=0.5, type=2, mul=self.amp).mix(1)

            self.mix = Mix([self.osc1, self.osc2], voices=2)

            self.damp = ButLP(self.mix, freq=5000)

            self.lfo = Sine(0.2, phase=[random(), random()]).range(250, 4000)
            self.notch = ButBR(self.damp, self.lfo, mul=mul)

        def out(self):
            self.notch.out()
            return self

        def sig(self):
            return self.notch
    s = Server()
    s.setMidiInputDevice(99)
    s.boot()
    s.start()
    synt = Synth().out()
    synt.note = (MidiFile("Data/sun.mid"))
    for message in synt.note.play():
        s.addMidiEvent(*message.bytes())
    s.gui(locals())


