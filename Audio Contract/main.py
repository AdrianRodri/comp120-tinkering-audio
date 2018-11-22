
'''
-------------------------------------------------------------------------------
This program will generate a melodic sound (sort of)
    created by Adrian Rodriguez
-------------------------------------------------------------------------------
'''

import time

import random
import sounddevice as sd
import NoteFreqDict

import WaveCalc
'''
-------------------------------------------------------------------------------
Samples per second
-------------------------------------------------------------------------------
'''
sps = 44100
'''
-------------------------------------------------------------------------------
Duration of each note
-------------------------------------------------------------------------------
'''
duration_secs = 1/8


'''
-------------------------------------------------------------------------------
Randomly Selects 5 Notes
-------------------------------------------------------------------------------
'''

keys = list(NoteFreqDict.NoteFreqDict.values())
keys.sort()
print(type(NoteFreqDict.NoteFreqDict))
starting_note = random.choice(list(NoteFreqDict.NoteFreqDict.values()))
print(starting_note)
current_pos = keys.index(starting_note)
next_pos = current_pos + random.randint(-1,1)

if next_pos > 0 or next_pos < len(keys):
    second_note = keys[next_pos]
else :
    current_pos = next_pos
print(second_note)

next_pos = current_pos + random.randint(-1,1)
if next_pos > 0 or next_pos < len(keys):
    third_note = keys[next_pos]
else :
    current_pos = next_pos
print(second_note)

next_pos = current_pos + random.randint(-1,1)
if next_pos > 0 or next_pos < len(keys):
    fourth_note = keys[next_pos]
else :
    current_pos = next_pos
print(second_note)

next_pos = current_pos + random.randint(-1,1)
if next_pos > 0 or next_pos < len(keys):
    fifth_note = keys[next_pos]
else :
    current_pos = next_pos
print(second_note)



'''
-------------------------------------------------------------------------------
Plays the waveform out of the speakers
-------------------------------------------------------------------------------
'''

sd.play(WaveCalc.attenuated_waveform_A4, sps)
time.sleep(duration_secs)
sd.stop()


