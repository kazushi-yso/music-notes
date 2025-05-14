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
    # "Fb": "E",
    # "E#": "F",
    # "F": "E#",
    # "B#": "C",
    # "C": "B#"    
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
        scale.append(note)
    return scale
#  first_index = scale_base.index(key)
#     return [scale_base[(first_index + i) % 12] for i in MAJOR_SCALE_INTERVALS]

def get_letter(note):
    for letter in "CDEFGAB":
        if note.startswith(letter):
            return letter
        return None
    
def check_natural_notes(scale):
    natural_notes = [get_letter(note) for note in scale]
    return len(set(natural_notes)) == 7

def choose_better_key(key):
    scale = build_major_scale(key)
    if not check_natural_notes(scale):
        alt_key = ENHARMONIC_KEYS.get(key)
        if alt_key:
            alt_scale = build_major_scale(alt_key)
            if check_natural_notes(alt_scale):
                return alt_key
        return key