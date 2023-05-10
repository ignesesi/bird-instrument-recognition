import string
from pathlib import Path

class AUDIO_CONFIG:
    sampling_rate = 32000
    duration = 1
    hop_length = 251 # making it 128 in size
    fmin = 500
    fmax = 15000
    n_mels = 128
    n_fft = n_mels * 20
    samples = sampling_rate * duration
    padmode = 'reflect'
    
def fill_range(letter_start, letter_end, path_fill, dict_val={}):
    alphabet = list(string.ascii_lowercase)
    for a in alphabet[alphabet.index(letter_start):alphabet.index(letter_end)+1]:
        dict_val[a] = path_fill
    return dict_val

def get_dict_value(input_dir):
    dict_val = {}
    path = "small-data-instruments/small_data_kaggle/train_audio"
    dict_val = fill_range('a','z',input_dir/path,dict_val)  
#    dict_val = fill_range('a','b',input_dir/"birdsong-resampled-train-audio-00",dict_val)
#    dict_val = fill_range('c','f',input_dir/"birdsong-resampled-train-audio-01",dict_val)
#    dict_val = fill_range('g','m',input_dir/"birdsong-resampled-train-audio-02",dict_val)
#    dict_val = fill_range('n','r',input_dir/"birdsong-resampled-train-audio-03",dict_val)
#    dict_val = fill_range('s','y',input_dir/"birdsong-resampled-train-audio-04",dict_val)
    return dict_val

BIRD_CODE = {
    'accordion': 0, 'bass_tuba': 1, 'bassoon': 2, 'clarinet': 3, 
    'contrabass': 4, 'flute': 5, 'horn': 6, 'oboe': 7, 'sax': 8,
    'trombone': 9, 'trumpet': 10, 'viola': 11, 'violin': 12, 'cello': 13
}

EBIRD_LABEL = {
    'accordion': 'Accordion', 'bass_tuba': 'Bass tuba', 'bassoon': 'Bassoon',
    'clarinet': 'Clarinet', 'contrabass': 'Contrabass', 'flute': 'Flure',
    'horn': 'Horn', 'oboe': 'Oboe', 'sax': 'Sax', 'trombone': 'Trombone',
    'trumpet': 'Trumpet', 'viola': 'Viola', 'violin': 'Violin', 'cello': 'Cello'
}

INV_EBIRD_LABEL = {v: k for k, v in EBIRD_LABEL.items()}
