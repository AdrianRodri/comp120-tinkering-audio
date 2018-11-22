import numpy as np

from NoteFreqDict import NoteFreqDict
'''
-------------------------------------------------------------------------------
Using Numpy to calculate all waveforms from NoteFreqDict.py
-------------------------------------------------------------------------------
'''
sps = 44100
duration_secs = 0.5
vol_multiplier = float(0.2)
each_sample_number = np.arange(duration_secs * sps )

waveform_A4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['A4'] / sps)
attenuated_waveform_A4 = waveform_A4 * vol_multiplier

waveform_A3 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['A3'] / sps)
attenuated_waveform_A3 = waveform_A3 * vol_multiplier

waveform_As4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['As4'] / sps)
attenuated_waveform_As4 = waveform_As4 * vol_multiplier

waveform_B4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['B4'] / sps)
attenuated_waveform_B4 = waveform_B4 * vol_multiplier

waveform_C4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['C4'] / sps)
attenuated_waveform_C4 = waveform_C4 * vol_multiplier

waveform_Cs4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['Cs4'] / sps)
attenuated_waveform_Cs4 = waveform_Cs4 * vol_multiplier

waveform_D4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['D4'] / sps)
attenuated_waveform_D4 = waveform_D4 * vol_multiplier

waveform_Ds4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['Ds4'] / sps)
attenuated_waveform_Ds4 = waveform_Ds4 * vol_multiplier

waveform_E4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['E4'] / sps)
attenuated_waveform_E4 = waveform_E4 * vol_multiplier

waveform_F4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['F4'] / sps)
attenuated_waveform_F4 = waveform_F4 * vol_multiplier

waveform_Fs4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['Fs4'] / sps)
attenuated_waveform_Fs4 = waveform_Fs4 * vol_multiplier

waveform_G4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['G4'] / sps)
attenuated_waveform_G4 = waveform_G4 * vol_multiplier

waveform_G3 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['G3'] / sps)
attenuated_waveform_G3 = waveform_G4 * vol_multiplier

waveform_Gs4 = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['Gs4'] / sps)
attenuated_waveform_Gs4 = waveform_G4 * vol_multiplier



