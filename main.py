if __name__ == "__main__":
    from pyo import *
    s = Server()
    s.setMidiInputDevice(0)
    s.boot()
    s.start()
    s.amp = 0.1
    midi = Notein()
    pitch = MToF(midi['pitch'])
    amp = MidiAdsr(midi['velocity'])
    wave = SquareTable()
    oscs = Osc(wave, mul=amp)
    d = Delay(oscs, delay=0.25, feedback=0, maxdelay=1, mul=1, add=0)
    d.ctrl(title='Delay')
    r = Freeverb(oscs, size=[.79, .8], damp=.9, bal=.3)
    r.ctrl(title='Reverb')
    s.gui(locals())


