
'''
-------------------------------------------------------------------------------
This program will generate a melodic sound (sort of)
    created by Adrian Rodriguez
-------------------------------------------------------------------------------
'''

import time
import numpy as np
import random
import sounddevice as sd
import NoteFreqDict
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
# Creates alist of the NoteFreqDict
keys = list(NoteFreqDict.NoteFreqDict.values())
keys.sort()
print(type(NoteFreqDict.NoteFreqDict))

# Randomly picks a starting note for the melody
starting_note = random.choice(list(NoteFreqDict.NoteFreqDict.values()))
print(starting_note)
current_pos = keys.index(starting_note)

# Checks item in the list of frequecies.
# Randomly chooses the item before or same or after.
# If the item is out of range of the list, we move double the distance in
# the other direction.

next_pos = current_pos + random.randint(-1,1)
if next_pos < 0 or next_pos < len(keys):
    second_note = keys[next_pos]
else :
    step = random.randint(-1, 1)
    next_pos = current_pos + 2 * (-step)
    second_note = next_pos
print(second_note)


if next_pos < 0 or next_pos < len(keys):
    third_note = keys[next_pos]
else :
    step = random.randint(-1, 1)
    next_pos = current_pos + 2 * (-step)
    third_note = next_pos
print(second_note)


next_pos = current_pos + random.randint(-1,1)
if next_pos < 0 or next_pos < len(keys):
    fourth_note = keys[next_pos]
else :
    step = random.randint(-1, 1)
    next_pos = current_pos + 2 * (-step)
    fourth_note = next_pos
print(fourth_note)


next_pos = current_pos + random.randint(-1,1)
if next_pos < 0 or next_pos < len(keys):
    fifth_note = keys[next_pos]
else :
    step = random.randint(-1, 1)
    next_pos = current_pos + 2 * (-step)
    fifth_note = next_pos
print(fifth_note)


'''
-------------------------------------------------------------------------------
Plays the waveform out of the speakers
-------------------------------------------------------------------------------
'''

each_sample_number = np.arange(duration_secs * sps )

# Setting a volume factor (adjustable volume)
vol_multiplier = float(0.8)

# Calculates 5 waves: a, b, c, d, and e
# then plays them one after the other, then the program stops

a_waveform = np.sin(2 * np.pi * each_sample_number * starting_note / sps)
attenuated_waveform_1 = a_waveform * vol_multiplier
sd.play(attenuated_waveform_1, sps)
time.sleep(duration_secs)

b_waveform = np.sin(2 * np.pi * each_sample_number * second_note / sps)
attenuated_waveform_2 = b_waveform * vol_multiplier
sd.play(attenuated_waveform_2, sps)
time.sleep(duration_secs)

c_waveform = np.sin(2 * np.pi * each_sample_number * third_note / sps)
attenuated_waveform_3 = c_waveform * vol_multiplier
sd.play(attenuated_waveform_3, sps)
time.sleep(duration_secs)

d_waveform = np.sin(2 * np.pi * each_sample_number * fourth_note / sps)
attenuated_waveform_4 = d_waveform * vol_multiplier
sd.play(attenuated_waveform_4, sps)
time.sleep(duration_secs)

e_waveform = np.sin(2 * np.pi * each_sample_number * fourth_note / sps)
attenuated_waveform_5 = e_waveform * vol_multiplier
sd.play(attenuated_waveform_5, sps)
time.sleep(duration_secs)

sd.stop()


