"""
This file contains the description of the "makams" and "usuls"

Sources:
http://adanamusikidernegi.com
http://www.hazimgokcen.net
http://www.channelingstudio.ru/texts/Music%20Theory%20of%20Makams.pdf
"""

USUL = {'aksak': [('dum', 1), ('te', 3), ('ke', 4), ('dum', 5), ('tek', 7), ('tek', 9)],
        'duyek': [('dum', 1), ('tek', 2), ('tek', 4), ('dum', 5), ('tek', 7)],
        'sofyan': [('dum', 1), ('te', 3), ('ke', 4)]}

USUL_TS = {'aksak': [('dum', '0000'), ('te', '2222'), ('ke', '3333'), ('dum', '4444'), ('tek', '6666'), ('tek', '8888')],
            'duyek': [('dum', '0000'), ('tek', '1250'), ('tek', '3750'), ('dum', '5000'), ('tek', '7500')],
            'sofyan': [('dum', '0000'), ('te', '5000'), ('ke', '7500')]}

MAKAM = {'hicaz': ['Dugah', 'Dik Kurdi', 'Nim Hicaz', 'Neva', 'Huseyni', 'Evic', 'Gerdaniye', 'Muhayyer'],
         'nihavent': ['Rast', 'Dugah', 'Kurdi', 'Cargah', 'Neva', 'Nim Hisar', 'Hisar', 'Acem', 'Evic', 'Gerdaniye'],
         'huzzam': ['Segah', 'Cargah', 'Neva', 'Hisar', 'Evic', 'Gerdaniye', 'Sunbule', 'Tiz Segah'],
         'ussak': ['Dugah', 'Segah', 'Cargah', 'Neva', 'Huseyni', 'Acem', 'Gerdaniye', 'Muhayyer'],
         'segah': ['Segah', 'Cargah', 'Neva', 'Dik Hisar', 'Evic', 'Gerdaniye', 'Sunbule', 'Tiz Segah'],
         'rast': ['Rast', 'Dugah', 'Segah', 'Cargah', 'Neva', 'Huseyni', 'Evic', 'Gerdaniye'],
         'mahur': ['Rast', 'Dugah', 'Buselik', 'Cargah', 'Neva', 'Huseyni', 'Mahur', 'Gerdaniye']}

ALL_NOTES = {'A3':'Kaba Kaba Dugah',
             'B-slash-flat3':'Kaba Kaba Dik Kurdi',
             'B-flat3':'Kaba Kaba Kurdi',
             'G3':'Kaba Rast',
             'A4':'Kaba Dugah',
             'A-sharp4':'Kaba Kurdi',
             'B-half-flat4': 'Kaba Segah',
             'B-slash-flat4':'Kaba Dik Kurdi',
             'B-flat4':'Kaba Kurdi',
             'B4':'Kaba Buselik',
             'C4':'Kaba Cargah',
             'C-sharp4':'Kaba Nim Hicaz',
             'C-slash-quarter-sharp4':'Kaba Hicaz',
             'C-slash-sharp4': 'Kaba Dik Hicaz',
             'D-flat4': 'Kaba Nim Hicaz',
             'D-slash-flat4':'Kaba Hicaz',
             'D-half-flat4':'Kaba Dik Hicaz',
             'D4':'Yegah',
             'D-sharp4':'Kaba Nim Hisar',
             'D-slash-quarter-sharp4':'Kaba Hisar',
             'D-slash-sharp4': 'Kaba Dik Hisar',
             'E-flat4': 'Kaba Nim Hisar',
             'E-slash-flat4':'Kaba Hisar',
             'E-half-flat4':'Kaba Dik Hisar',
             'E4':'Huseyni Asiran',
             'F4':'Acem Asiran',
             'F-quarter-sharp4':'Dik Acem Asiran',
             'F-sharp4':'Irak',
             'F-slash-quarter-sharp4':'Gevest',
             'F-slash-sharp4':'Dik Gevest',
             'G-double-slash-flat4':'Dik Acem Asiran',
             'G-flat4':'Irak',
             'G-slash-flat4':'Gevest',
             'G-half-flat4':'Dik Gevest',
             'G4':'Rast',
             'G-sharp4': 'Nim Zirgule',
             'G-slash-quarter-sharp4':'Zirgule',
             'G-slash-sharp4':'Dik Zirgule',
             'A-flat5':'Nim Zirgule',
             'A-slash-flat5':'Zirgule',
             'A-half-flat5':'Dik Zirgule',
             'A5':'Dugah',
             'A-sharp5':'Kurdi',
             'A-slash-quarter-sharp5':'Dik Kurdi',
             'A-slash-sharp5':'Segah',
             'B-flat5':'Kurdi',
             'B-slash-flat5':'Dik Kurdi',
             'B-half-flat5':'Segah',
             'B5':'Buselik',
             'C-half-flat5':'Dik Buselik',
             'C5':'Cargah',
             'C-sharp5':'Nim Hicaz',
             'C-slash-quarter-sharp5':'Hicaz',
             'C-slash-sharp5':'Dik Hicaz',
             'D-flat5': 'Nim Hicaz',
             'D-slash-flat5':'Hicaz',
             'D-half-flat5':'Dik Hicaz',
             'D5':'Neva',
             'D-sharp5':'Nim Hisar',
             'D-slash-quarter-sharp5':'Hisar',
             'D-slash-sharp5':'Dik Hisar',
             'E-flat5':'Nim Hisar',
             'E-slash-flat5':'Hisar',
             'E-half-flat5':'Dik Hisar',
             'E5':'Huseyni',
             'E-sharp5':'Acem',
             'F5':'Acem',
             'F-quarter-sharp5':'Dik Asem',
             'F-sharp5':'Evic',
             'F-slash-quarter-sharp5':'Mahur',
             'F-slash-sharp5':'Dik Mahur',
             'G-double-slash-flat5':'Dik Asem',
             'G-flat5':'Evic',
             'G-slash-flat5':'Mahur',
             'G-half-flat5':'Dik Mahur',
             'G5':'Gerdaniye',
             'G-sharp5':'Nim Sehnaz',
             'G-slash-quarter-sharp5':'Sehnaz',
             'G-slash-sharp5':'Dik Sehnaz',
             'A-flat6': 'Nim Sehnaz',
             'A-slash-flat6':'Sehnaz',
             'A-half-flat6':'Dik Sehnaz',
             'A6':'Muhayyer',
             'A-sharp6':'Sunbule',
             'A-slash-quarter-sharp6':'Dik Sunbule',
             'A-slash-sharp6':'Tiz Segah',
             'B-flat6':'Sunbule',
             'B-slash-flat6':'Dik Sunbule',
             'B-half-flat6':'Tiz Segah',
             'B6': 'Tiz Buselik',
             'C-half-flat6':'Tiz Dik Buselik',
             'C6':'Tiz Cargah',
             'C-sharp6':'Tiz Nim Hicaz',
             'D6':'Tiz Neva',
             'E6':'Tiz Huseyni'
}

ALL_NOTES_TXT = {'A3':'Kaba Kaba Dugah',
                 'B3b4':'Kaba Kaba Dik Kurdi',
                 'B3b5':'Kaba Kaba Kurdi',
                 'G3':'Kaba Rast',
                 'A4':'Kaba Dugah',
                 'A4#4':'Kaba Kurdi',
                 'B4b1': 'Kaba Segah',
                 'B4b4':'Kaba Dik Kurdi',
                 'B4b5':'Kaba Kurdi',
                 'B4':'Kaba Buselik',
                 'C4':'Kaba Cargah',
                 'C4#4':'Kaba Nim Hicaz',
                 'C4#5':'Kaba Hicaz',
                 'C4#8': 'Kaba Dik Hicaz',
                 'D4b5': 'Kaba Nim Hicaz',
                 'D4b4':'Kaba Hicaz',
                 'D4b1':'Kaba Dik Hicaz',
                 'D4':'Yegah',
                 'D4#4':'Kaba Nim Hisar',
                 'D4#5':'Kaba Hisar',
                 'D4#8': 'Kaba Dik Hisar',
                 'E4b5': 'Kaba Nim Hisar',
                 'E4b4':'Kaba Hisar',
                 'E4b1':'Kaba Dik Hisar',
                 'E4':'Huseyni Asiran',
                 'F4':'Acem Asiran',
                 'F4#1':'Dik Acem Asiran',
                 'F4#4':'Irak',
                 'F4#5':'Gevest',
                 'F4#8':'Dik Gevest',
                 'G4b8':'Dik Acem Asiran',
                 'G4b5':'Irak',
                 'G4b4':'Gevest',
                 'G4b1':'Dik Gevest',
                 'G4':'Rast',
                 'G4#4': 'Nim Zirgule',
                 'G4#5':'Zirgule',
                 'G4#8':'Dik Zirgule',
                 'A5b5':'Nim Zirgule',
                 'A5b4':'Zirgule',
                 'A5b1':'Dik Zirgule',
                 'A5':'Dugah',
                 'A5#4':'Kurdi',
                 'A5#5':'Dik Kurdi',
                 'A5#8':'Segah',
                 'B5b5':'Kurdi',
                 'B5b4':'Dik Kurdi',
                 'B5b1':'Segah',
                 'B5':'Buselik',
                 'C5b1':'Dik Buselik',
                 'C5':'Cargah',
                 'C5#4':'Nim Hicaz',
                 'C5#5':'Hicaz',
                 'C5#8':'Dik Hicaz',
                 'D5b5': 'Nim Hicaz',
                 'D5b4':'Hicaz',
                 'D5b1':'Dik Hicaz',
                 'D5':'Neva',
                 'D5#4':'Nim Hisar',
                 'D5#5':'Hisar',
                 'D5#8':'Dik Hisar',
                 'E5b5':'Nim Hisar',
                 'E5b4':'Hisar',
                 'E5b1':'Dik Hisar',
                 'E5':'Huseyni',
                 'E5#4':'Acem',
                 'F5':'Acem',
                 'F5#1':'Dik Acem',
                 'F5#4':'Evic',
                 'F5#5':'Mahur',
                 'F5#8':'Dik Mahur',
                 'G5b8':'Dik Acem',
                 'G5b5':'Evic',
                 'G5b4':'Mahur',
                 'G5b1':'Dik Mahur',
                 'G5':'Gerdaniye',
                 'G5#4':'Nim Sehnaz',
                 'G5#5':'Sehnaz',
                 'G5#8':'Dik Sehnaz',
                 'A6b5': 'Nim Sehnaz',
                 'A6b4':'Sehnaz',
                 'A6b1':'Dik Sehnaz',
                 'A6':'Muhayyer',
                 'A6#4':'Sunbule',
                 'A6#5':'Dik Sunbule',
                 'A6#8':'Tiz Segah',
                 'B6b5':'Sunbule',
                 'B6b4':'Dik Sunbule',
                 'B6b1':'Tiz Segah',
                 'B6': 'Tiz Buselik',
                 'C6b1':'Tiz Dik Buselik',
                 'C6':'Tiz Cargah',
                 'C6#4':'Tiz Nim Hicaz',
                 'D6':'Tiz Neva',
                 'E6':'Tiz Huseyni'
}
