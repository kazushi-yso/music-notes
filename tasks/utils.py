ENHARMONIC_KEYS = {
    "C#": "Db",
    "Db": "C#",
    "D#": "Eb",
    "Eb": "D#",
    "F#": "Gb",
    "Gb": "F#",
    "G#": "Ab",
    "Ab": "G#",
    "A#": "Bb",
    "Bb": "A#",
    "B": "Cb",
    "Cb": "B",
    "E": "Fb",
    "Fb": "E"
}

CHROMATIC_SCALE_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
CHROMATIC_SCALE_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
MAJOR_SCALE_INTERVALS = [0, 2, 4, 5, 7, 9, 11]

def build_major_scale(key):
    if key in CHROMATIC_SCALE_SHARP:
        scale_base = CHROMATIC_SCALE_SHARP
    elif key in CHROMATIC_SCALE_FLAT:
        scale_base = CHROMATIC_SCALE_FLAT
    else:
        return []
    
    scale = []
    for i in MAJOR_SCALE_INTERVALS:
        first_index = scale_base.index(key)
        note_index = (first_index + i) % 12
        note = scale_base[note_index]
        scale.apennd(note)
    return scale
#  first_index = scale_base.index(key)
#     return [scale_base[(first_index + i) % 12] for i in MAJOR_SCALE_INTERVALS]

def has_double_accidentals(scale):
    for note in scale:
        if '##' in note or 'bb' in note:
            return True   
# return any("##" in note or "bb" in note for note in scale)
