import os

from mu_Info import *
from score_handler import *
import matplotlib.pyplot as plt
import numpy as np

# Look at the filenames within this directory
makamUsul_dict = dict()
print('Reading data ...')
print('Looking for makam-usul combinations')
for root, dirs, files in os.walk('./SymbTr-2.0.0'):
    for file in files:
        # skip non ".txt" files
        if '.txt' not in file:
            continue
        sfile = file.split('--')
        # skip not correctly formated file names
        if len(sfile) < 3:
            continue
        # count the occurrencies of every combinations of makam-usul
        mu_key = sfile[0]+'--'+sfile[2]
        makamUsul_dict[mu_key] = makamUsul_dict.get(mu_key,0) + 1
print(len(makamUsul_dict), 'different combinations of makam-usul found')
#
mu_top = sorted(makamUsul_dict, key = makamUsul_dict.get, reverse = True)[0:10]
print('\nTop 10 combinations:')
[print(mu) for mu in mu_top]
print('\nSelecting the files with the desired makam-usul combination')
f_dict = dict()
for root, dirs, files in os.walk('./SymbTr-2.0.0'):
    for file in files:
        # skip non ".xml" files
        if '.txt' not in file:
            continue
        sfile = file.split('--')
        # skip not correctly formated file names
        if len(sfile) < 3:
            continue
        mu_key = mu_key = sfile[0]+'--'+sfile[2]
        if mu_key in mu_top:
            f_dict[root+'/'+file] = {'group': mu_key, 'makam': sfile[0], 'usul': sfile[2]}
print(len(f_dict), 'scores will be computed')
print('Starting the score analysis ...')
beat_dict = dict()
for file, values in f_dict.items():
    # beat_dict contains the whole structure
    # the first level are dictionaries by combination
    beat_dict[values['group']] = beat_dict.get(values['group'], dict())
    usul = USUL_TS[values['usul']]
    beat_dict[values['group']] = get_notes_on_beat_txt(file, usul, beat_dict[values['group']])
print('Score analysis: DONE')
top_dict = dict()
for mu in mu_top:
    top_dict[mu] = dict()
    makam = mu.split('--')[0]
    usul = USUL_TS[mu.split('--')[1]]
    beat_name = [a[0]+'_{}'.format(a[1]) for a in usul]
    print('\nMost common notes of the makam {} on the usul`s beat {}:'.format(makam, mu.split('--')[1]))
    for beat in beat_name:
        top_notes = sorted(beat_dict[mu][beat], key = beat_dict[mu][beat].get, reverse = True)[0:3]
        top_dict[mu][beat] = [(note, beat_dict[mu][beat][note]) for note in top_notes]
        print(beat, top_dict[mu][beat])
    print(makam, 'notes:')
    print(MAKAM[makam])

# plotting
bar_width = 0.35
for mu in mu_top:
    # import ipdb; ipdb.set_trace()
    fig, ax = plt.subplots(figsize = (15,10))
    makam_notes = MAKAM[mu.split('--')[0]]
    usul = USUL_TS[mu.split('--')[1]]
    n_groups = len(usul)
    index = np.arange(n_groups)*bar_width*(1+len(makam_notes))
    beat_name = [a[0]+'_{}'.format(a[1]) for a in usul]
    for note in makam_notes:
        occu = tuple([beat_dict[mu][beat].get(note, 0) for beat in beat_name])
        rects = ax.bar(index, occu, bar_width, label=note)
        index = index + bar_width
    ax.set_xlabel('beat')
    ax.set_ylabel('occurrence')
    ax.set_title(mu.upper())
    ax.set_xticks( np.arange(n_groups)*bar_width*(1+len(makam_notes)) + bar_width*(len(makam_notes))/2)
    ax.set_xticklabels(tuple(beat_name))
    ax.legend()
    fig.tight_layout()
    plt.savefig('./generated_histograms/'+mu, format = 'png')
    plt.show()
