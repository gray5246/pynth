if __name__ == "__main__":
    from pyo import *
    from random import random
    from mido import MidiFile
    import instruments
    def playfile(file, instrument):
        instrument.note = (MidiFile(file))
        for message in instrument.note.play():
            s.addMidiEvent(*message.bytes())
    s = Server()
    s.setMidiInputDevice(99)
    s.boot()
    s.start()
    synt = instruments.BasicOsc().out()
    synt.controller()
    pm_list_devices()
    s.gui(locals())


