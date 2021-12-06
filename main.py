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
                    s.start()
                    s.gui(locals())
                    wantsynth = True

        screen.fill((60, 25, 60))

        mouse = pygame.mouse.get_pos()

        if mouse[0] in range(200, 600) and mouse[1] in range(200, 600):
            pygame.draw.polygon(screen, color_light, [(200, 200), (200, 600), (600, 400)])

        else:
            pygame.draw.polygon(screen, color_dark, [(200, 200), (200, 600), (600, 400)])

        screen.blit(text, (250, 370))
        if wantsynth == True:
            synt = instruments.BasicOsc().out()
            synt.controller()
        pygame.display.update()



