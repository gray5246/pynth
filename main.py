if __name__ == "__main__":
    from pyo import *
    import pygame
    import sys
    import random
    from mido import MidiFile
    import instruments
    s = Server().boot()

    class BasicOscInst(EventInstrument):
        def self(self, **args):
            EventInstrument.__init__(self, **args)

            # self.freq is derived from the 'degree' argument.
            self.phase = Phasor([self.freq, self.freq * 1.003])

            # self.dur is derived from the 'beat' argument.
            self.duty = Expseg([(0, 0.05), (self.dur, 0.5)], exp=4).play()

            self.osc = Compare(self.phase, self.duty, mode="<", mul=1, add=-0.5)

            # EventInstrument created the amplitude envelope as self.env.
            self.filt = ButLP(self.osc, freq=5000, mul=self.env).out()


    #rander = random.choice([2, 4, 3, 8])
    choice = EventChoice(instruments.choosekey())
    beate = EventChoice([1/4, 1/4, 1/2, 1/2, 1/2, 1, 2, 1, 2])
    bchoice = choice - 12
    #env = MidiAdsr(choice, attack=0.001, decay=0.05, sustain=0.7, release=0.1, mul=0.1, )
    bpm = random.randrange(80, 150)
    #fr = MToF(mid, mul=env)
    #fd = Randi(min=0, max=0.05, freq=1)
    sp = RandInt(max=4, freq=1, add=2)
    amp = Sine(sp, mul=0.2, add=0.2)
    #event = Events(instrument=BasicOscInst, midinote=choice, beat=beate, amp=amp, attack=0.001, decay=0.05, sustain=0.5, release=0.005).play()
    e = Events(
        midinote=choice,
        beat=beate,
        amp=amp,
        bpm=bpm,
        attack=0.001,
        decay=0.05,
        sustain=0.5,
        release=0.005,
    ).play()
    be = Events(
        midinote=bchoice,
        beat=1,
        db=-12,
        bpm=bpm,
        attack=0.001,
        decay=0.05,
        sustain=0.5,
        release=0.005,
    ).play()
    s.start()
    s.gui(locals())


