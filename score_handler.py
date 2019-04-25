import xml.etree.ElementTree as ET
from music21 import *
from mu_Info import *
import csv

def clean_xml(root, file, output_folder):
    if not output_folder.endswith('/'):
        output_folder += '/'
    tree = ET.parse(root+'/'+file)
    root = tree.getroot()

    for k in root.iter('key'):
        for ks in k.findall('key-step'):
            k.remove(ks)
        for ka in k.findall('key-accidental'):
            k.remove(ka)
        for ka in k.findall('key-alter'):
            k.remove(ka)

    n_file = output_folder + file[:-4] + 'noKeySig.xml'
    tree.write(n_file)
    return n_file

def get_parts(file):
    try:
        s = converter.parse(file)
        pp = s.parts
    except:
        print('review this file:', file)
        pp = list()
    return pp

def get_notes_on_beat(p, usul, beat_dict, pr = False):
    nn = p.flat.notes.stream()
    m0 = p.getElementsByClass(stream.Measure).stream()[0]
    tS = m0.getElementsByClass(meter.TimeSignature).stream()[0]
    m_length = tS.numerator*(4/tS.denominator)
    beat_name = [a[0]+'_{}'.format(a[1]) for a in usul]
    beats = [a[1] for a in usul]
    for n in nn:
        if pr: print(n.fullName)
        beat_pos = 2*(n.offset % m_length) + 1
        if beat_pos in beats:
            n_pitch_name = n.fullName.split()[0]+n.fullName.split()[3]
            if pr: print('ON BEAT:', n_pitch_name)
            note_name = ALL_NOTES.get(n_pitch_name, n_pitch_name)
            beat_tag = beat_name[beats.index(beat_pos)]
            beat_dict[beat_tag] = beat_dict.get(beat_tag, dict())
            beat_dict[beat_tag][note_name] = beat_dict[beat_tag].get(note_name, 0) + 1
    return beat_dict

def get_notes_on_beat_txt(file, usul, beat_dict, pr = False):
    first_line = True
    offset = '000000'
    beat_name = [a[0]+'_{}'.format(a[1]) for a in usul]
    beats = [a[1] for a in usul]
    with open(file) as f:
        reader = csv.reader(f)
        for line in reader:
            if first_line:
                first_line = False
                continue
            s_line = line[0].split()
            if int(s_line[6]) == 0:
                continue
            if s_line[3] == 'Es':
                continue
            if offset in beats:
                n_pitch_name = s_line[3]
                if pr: print('ON BEAT:', n_pitch_name)
                note_name = ALL_NOTES_TXT.get(n_pitch_name, n_pitch_name)
                beat_tag = beat_name[beats.index(offset)]
                beat_dict[beat_tag] = beat_dict.get(beat_tag, dict())
                beat_dict[beat_tag][note_name] = beat_dict[beat_tag].get(note_name, 0) + 1
            offset = s_line[-1].split('.')[1][:4]
    return beat_dict

def notes_on_file(file):
    sfile = file.split('--')
    mu_key = mu_key = sfile[0]+'--'+sfile[2]
    values = {'group': mu_key, 'makam': sfile[0], 'usul': sfile[2]}

    beat_dict = dict()
    beat_dict[values['group']] = beat_dict.get(values['group'], dict())
    pp = get_parts(file)
    usul = USUL[values['usul']]
    for p in pp:
        beat_dict[values['group']] = get_notes_on_beat(p, usul, beat_dict[values['group']], pr = True)
