import pickle
import glob

def splitline_all(): # 모든 가사 줄바꿈 기준으로 전부 분리해서 list에 넣기

    result = []

    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyrics.pickle')
    with open(ret[0], 'rb') as f: bal = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\rnb_lyrics.pickle')
    with open(ret[0], 'rb') as f: rnb = pickle.load(f)

    lyrics = bal + rnb

    for i in lyrics:
        result += i.split('\n')

    # print(result)
    # print(len(result))

    return result

def splitline_part(): # 시작 가사, 끝 가사 전부 분리해서 list에 넣기

    result = []

    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyrics_end.pickle')
    with open(ret[0], 'rb') as f: bal_ed = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\rnb_lyrics_end.pickle')
    with open(ret[0], 'rb') as f: rnb_ed = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyrics_start.pickle')
    with open(ret[0], 'rb') as f: bal_op = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\rnb_lyrics_start.pickle')
    with open(ret[0], 'rb') as f: rnb_op = pickle.load(f)

    lyrics = bal_op + rnb_op + bal_ed + rnb_ed

    # print(result)
    # print(len(result))

    return result

