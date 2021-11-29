if __name__ == "__main__":
    from pyo import *
    s = Server()
    #call midi stuff here
    s.boot()
    s.start()
    s.amp = 0.1
    oscs = Sine([300, 375, 500], mul=0.6).out()
    oscs.ctrl(title="B")
    s.gui(locals())
    (names, indexes) = pm_get_output_devices()
    name = names[indexes.index(pm_get_default_output())]
    print(name)

