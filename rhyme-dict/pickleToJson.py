import json
import glob
import pickle

# # 데이터를 로드합니다.
# ret = glob.glob('original\\rnb_lyrics_start.pickle')
# with open(ret[0], 'rb') as f: 
#     rnb_st = pickle.load(f)

# ret = glob.glob('original\\rnb_lyrics_end.pickle')
# with open(ret[0], 'rb') as f: 
#     rnb_ed = pickle.load(f)

# ret = glob.glob('original\\bal_lyrics_start.pickle')
# with open(ret[0], 'rb') as f: 
#     bal_st = pickle.load(f)

# ret = glob.glob('original\\bal_lyrics_end.pickle')
# with open(ret[0], 'rb') as f: 
#     bal_ed = pickle.load(f)

ret = glob.glob('original\\끄투 모든 단어 정제*')
with open(ret[0], 'rb') as f: 
    kkutuWords = pickle.load(f)

# # 데이터를 JSON 형식으로 변환하고 UTF-8 인코딩을 적용합니다.
# rnb_st_json = json.dumps(rnb_st, ensure_ascii=False).encode('utf-8')
# rnb_ed_json = json.dumps(rnb_ed, ensure_ascii=False).encode('utf-8')
# bal_st_json = json.dumps(bal_st, ensure_ascii=False).encode('utf-8')
# bal_ed_json = json.dumps(bal_ed, ensure_ascii=False).encode('utf-8')
kkutuWords_json = json.dumps(kkutuWords, ensure_ascii=False).encode('utf-8')

# # JSON 데이터를 파일로 저장합니다.
# with open('rnb_lyrics_start.json', 'wb') as f:
#     f.write(rnb_st_json)

# with open('rnb_lyrics_end.json', 'wb') as f:
#     f.write(rnb_ed_json)

# with open('bal_lyrics_start.json', 'wb') as f:
#     f.write(bal_st_json)

# with open('bal_lyrics_end.json', 'wb') as f:
#     f.write(bal_ed_json)

with open('kkutuWords.json', 'wb') as f:
    f.write(kkutuWords_json)
