if __name__ == "__main__":
    from pyo import *
    import pygame
    import sys
    import random
    from mido import MidiFile
    import instruments
    s = Server().boot()
    choice = EventChoice(instruments.choosekey())
    beate = EventChoice([1/4, 1/4, 1/2, 1/2, 1/2, 1, 2, 1, 2])
    bchoice = choice - 12
    bpm = random.randrange(80, 150)
    sp = RandInt(max=4, freq=1, add=2)
    amp = Sine(sp, mul=0.2, add=0.2)
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


