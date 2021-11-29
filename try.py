from pyo import *
s = Server().boot()
s.start()
env = CosTable([(0,0.0),(64,1.0),(8191,0.0)])
scl = EventScale(root="C", scale="egyptian", first=4, octaves=3)
seg = RandInt(max=6, freq=0.5)
step = RandInt(max=6, freq=0.75, add=-3)
note = EventSlide(scl, seg, step)
e = Events(midinote=note, beat=1/4., db=[-3, -9, -9], envelope=env, durmul=1.25).play()