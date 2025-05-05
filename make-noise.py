import tones.mixer

mixer = tones.mixer.Mixer()
mixer.create_track('yes')
mixer.add_note('yes', note="c#", endnote="d#", duration=0.65, octave=5)
mixer.write_wav('yes.wav')

mixer = tones.mixer.Mixer()
mixer.create_track('non')
mixer.add_note('non', note="d#", endnote="d#", duration=0.35, octave=2)
mixer.write_wav('non.wav')
