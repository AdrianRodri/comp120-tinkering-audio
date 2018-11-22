def WaveformCalc():
    sps = 44100
    duration_secs = 0.5
    vol_multiplier = float(0.2)
    each_sample_number = np.arange(duration_secs * sps)
    new_waveform = np.sin(2 * np.pi * each_sample_number * NoteFreqDict['A4'] / sps)
    attenuated_waveform_output = new_waveform * vol_multiplier
