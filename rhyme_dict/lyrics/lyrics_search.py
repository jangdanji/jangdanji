import glob
import pickle
import re

ret = glob.glob(f'rhyme_dict\\lyrics\\rnb_lyrics.pickle')
with open(ret[0], 'rb') as f: rnb = pickle.load(f)

while True:

    print('가사 데이터에서 찾을 ')

for r in rnb:
    re.findall()