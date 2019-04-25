import os

from mu_Info import *
from score_handler import *

file = './selected_scores/mahur--sarki--aksak--acirim_asik--giriftzen_asim_beynoKeySig.xml'
def notes_on_file(file):
    sfile = file.split('--')
    mu_key = mu_key = sfile[0]+'--'+sfile[2]
    values = {'group': mu_key, 'makam': sfile[0], 'usul': sfile[2]}

    beat_dict = dict()
    beat_dict[values['group']] = beat_dict.get(values['group'], dict())
    pp = get_parts(file)
    usul = USUL[values['usul']]
    for p in pp:
        beat_dict[values['group']] = get_notes_on_beat(p, usul, beat_dict[values['group']], p = True)
