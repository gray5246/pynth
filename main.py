if __name__ == "__main__":
    from pyo import *
    import pygame
    import sys
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
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Music Box")
    running = True
    width = 800
    height = 800
    color = (255, 255, 255)
    color_light = (0, 170, 0)
    color_dark = (0, 100, 0)
    smallfont = pygame.font.SysFont('Corbel', 60, bold=True)
    text = smallfont.render('START', True, color)
    while running:
        wantsynth = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] in range(200, 600) and mouse[1] in range(200, 600):
                    wantsynth = True

        screen.fill((60, 25, 60))

        mouse = pygame.mouse.get_pos()

        if mouse[0] in range(200, 600) and mouse[1] in range(200, 600):
            pygame.draw.polygon(screen, color_light, [(200, 200), (200, 600), (600, 400)])

        else:
            pygame.draw.polygon(screen, color_dark, [(200, 200), (200, 600), (600, 400)])

        screen.blit(text, (250, 370))
        if wantsynth == True:
            from pyo import *

            s = Server().boot()

            # Two streams of midi pitches chosen randomly in a predefined list.
            # The argument `choice` of Choice object can be a list of lists to
            # list-expansion.
            mid = Choice(choice=[50, 54, 56, 57, 61], freq=[4, 2])

            env = MidiAdsr(mid, attack=0.001, decay=0.05, sustain=0.7, release=0.1, mul=0.1, )
            # Converts midi pitches to frequencies and applies the jitters.
            fr = MToF(mid, mul=env)

            # Chooses a new feedback value, between 0 and 0.15, every 4 seconds.
            fd = Randi(min=0, max=0.15, freq=0.25)

            # RandInt generates a pseudo-random integer number between 0 and `max`
            # values at a frequency specified by `freq` parameter. It holds the
            # value until the next generation.
            # Generates an new LFO frequency once per second.
            sp = RandInt(max=6, freq=1, add=8)
            # Creates an LFO oscillating between 0 and 0.4.
            amp = Sine(sp, mul=0.2, add=0.2)

            # A simple synth...
            a = SineLoop(freq=fr, feedback=fd, mul=amp).out()
            s.start()
            s.gui(locals())
        pygame.display.update()



