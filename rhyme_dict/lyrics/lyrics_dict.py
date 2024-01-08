import pickle
import glob






print('가사의 앞 문장, 뒷 문장만 원하시면 1')
print('모든 가사를 원하시면 2를 입력하세요')

inp = str(input())

if inp == '1':

    print('어떤 단어를 검색하시겠어요?')

    word = str(input())

    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyrics_start.pickle')
    with open(ret[0], 'rb') as f: bal_st = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyrics_end.pickle')
    with open(ret[0], 'rb') as f: bal_ed = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\rnb_lyrics_start.pickle')
    with open(ret[0], 'rb') as f: rnb_st = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\rnb_lyrics_end.pickle')
    with open(ret[0], 'rb') as f: rnb_ed = pickle.load(f)

    all_lyrics = bal_st + bal_ed + rnb_st + rnb_ed

    print(len(all_lyrics))

    # print(all_lyrics)

    for i in all_lyrics:
        if word in i:
            print(i)

elif inp == '2':

    
    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyric.pickle')
    with open(ret[0], 'rb') as f: bal_st = pickle.load(f)

    ret = glob.glob('rhyme_dict\\lyrics\\bal_lyrics_end.pickle')
    with open(ret[0], 'rb') as f: bal_ed = pickle.load(f)