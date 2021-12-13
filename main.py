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
    def choosekeys():
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
        if "minor" in lister:
            return [38, 40, 41, 43, 46, 48]
        if "chord" in lister:
            return [[50, 54, 57, 59], [47, 50, 54, 57]]
        nl = []
        ok = False
        while ok != True:
            try:
                for ent in lister:
                    nl.append(int(ent))
            except ValueError as e:
                print("You mistyped a number or entered a non-number character.")
            ok = True
        return nl
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

            rander = random.choice([2, 4, 3, 8])
            mid = Choice(choice=choosekeys(), freq=[rander])
            env = MidiAdsr(mid, attack=0.001, decay=0.05, sustain=0.7, release=0.1, mul=0.1, )
            fr = MToF(mid, mul=env)
            fd = Randi(min=0, max=0.05, freq=0.25)
            sp = RandInt(max=1, freq=1, add=2)
            amp = Sine(sp, mul=0.2, add=0.2)
            a = SineLoop(freq=fr, feedback=fd, mul=0.1).out()

            osc1 = LFO(fr, type=1, mul=0.1).mix(1)

            mix = Mix([osc1], voices=1)

            damp = ButLP(mix, freq=5000)

            notch = ButBR(damp, mul=1).out()
            screen.fill((255, 255, 255))
            s.start()
            s.gui(locals())
            pass
        pygame.display.update()



