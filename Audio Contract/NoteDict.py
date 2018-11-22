import numpy as np

'''
-------------------------------------------------------------------------------
Single musical notes dictionary
-------------------------------------------------------------------------------
'''


NoteDict = {}

NoteDict['A'] = sps = 44100
frequency_hz = 440.0
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation

NoteDict['A#'] = sps = 44100
frequency_hz = 466.16
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation


NoteDict['B'] = sps = 44100
frequency_hz = 493.00
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation


NoteDict['C'] = sps = 44100
frequency_hz = 261.63
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation


NoteDict['C#'] = sps = 44100
frequency_hz = 277.18
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation


NoteDict['D'] = sps = 44100
frequency_hz = 293.66
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation

NoteDict['E'] = sps = 44100
frequency_hz = 329.63
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation


NoteDict['F'] = sps = 44100
frequency_hz = 349.23
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation


NoteDict['G'] = sps = 44100
frequency_hz = 293.66
duration_sec = 4.0
attenuation = 0.2

each_sample_number = np.arange(duration_sec * sps )
waveform = np.sin(2 * np.pi * each_sample_number * frequency_hz / sps)
attenuated_waveform = waveform * attenuation

