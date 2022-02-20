# This contains code for basic metric calculations

import numpy as np

def get_oaspl(waveform,reference = 20e-6):
    
    return 20 * np.log10(np.std(waveform)/reference)
