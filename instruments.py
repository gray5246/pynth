from pyo import *
class BasicOsc:
    def __init__(self, transpo=1, mul=1):
        self.transpo = Sig(transpo)
        self.note = Notein(poly=10, scale=1, first=0, last=127)
        self.mid = Choice(choice=choosekeys(), freq=[1, 1])

        self.pit = self.note["pitch"] * self.transpo
        self.amp = MidiAdsr(self.note["velocity"], attack=0.001, decay=0.05, sustain=0.7, release=0.1, mul=0.1, )

        self.osc1 = LFO(self.pit, sharp=0.5, type=2, mul=self.amp).mix(1)

        self.mix = Mix([self.osc1], voices=1)

        self.damp = ButLP(self.mix, freq=5000)

        self.notch = ButBR(self.damp, mul=mul)
    def out(self):
        self.notch.out()
        return self
    def controller(self):
        self.amp.ctrl(title='Envelope')
    def sig(self):
        return self.notch