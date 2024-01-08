import chrome
import glob
import pickle
import time

dv = chrome.startchrome()

def save_pickle(urls, name):
    with open(f"rhyme_dict\\lyrics\\{name}.pickle", 'wb') as f:
        pickle.dump(urls, f, pickle.HIGHEST_PROTOCOL)

# ret = glob.glob(f'rhyme_dict\\lyrics\\rnb_lyrics_link.pickle')
# with open(ret[0], 'rb') as f: rnb_link = pickle.load(f)

ret = glob.glob(f'rhyme_dict\\lyrics\\ballad_lyrics_link.pickle')
with open(ret[0], 'rb') as f: ballad_link = pickle.load(f)

lyrics = []
count = 0

# rnb_link = rnb_link[0:10]
# ballad_link = ballad_link[0:10]

for bal in ballad_link:

    print(str(count) +  ' / ' + str(len(ballad_link)))

    try:
        dv.get(bal)

        title = dv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[1]/div[1]').text
        artist = dv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[1]/div[2]').text
        lyric = dv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/div[2]/div').text

        # print(name)
        # print(artist)
        # print(lyric)

        lyrics.append(title + ' (' + artist + ')\n' + lyric)
        count += 1
    except:
        print('something wrong')
        
        time.sleep(660) # 11분
        lyrics.append(bal) # 크롤링 실패
        count += 1

save_pickle(lyrics, 'bal_lyrics')

