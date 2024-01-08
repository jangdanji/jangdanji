import chrome
import re
import time
import pickle

def save_pickle(urls, name):
    with open(f"C:\\Users\\01271\\Documents\\Github\\jonathan\\rhyme_dict\\lyrics\\{name}", 'wb') as f:
    # with open("C:\\Users\\NADANN\\Documents\\jonathan\\rhyme_dict\\lyrics\\lyrics_links.pickle", 'wb') as f:
        pickle.dump(urls, f, pickle.HIGHEST_PROTOCOL)

dv = chrome.startchrome()

pg = 0
firstNum = 1

urls = []

# 발라드 f'https://www.melon.com/genre/song_list.htm#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=NEW&params%5BsteadyYn%5D=N&po=pageObj&startIndex={pg*50+1}'

while True:

    dv.get(f'https://www.melon.com/genre/song_list.htm?gnrCode=GN0400#params%5BgnrCode%5D=GN0400&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=NEW&params%5BsteadyYn%5D=N&po=pageObj&startIndex={pg*50+1}')

    while True: # 페이지가 넘어갔는지 체크하는 과정 (맨 처음 노래번호가 +50이 되었는가)

        firstNum2 = dv.find_element_by_xpath('/html/body/div/div[3]/div/div/div[5]/form/div/table/tbody/tr[1]/td[2]/div/span[1]').text
    
        if 50 * pg + firstNum == int(firstNum2):
            break
        
        else:
            time.sleep(0.5)
    
    for i in range(1, 51):
        songNum = dv.find_element_by_xpath(f'/html/body/div/div[3]/div/div/div[5]/form/div/table/tbody/tr[{i}]/td[4]/div/a').get_attribute('href')
        songNum = re.findall('\'[0-9]+\'', songNum)
        link = 'https://www.melon.com/song/detail.htm?songId=' + str(re.sub('\'', '', songNum[0]))
        urls.append(link)
        print(link)
    
    pg += 1

    print(str(pg) + '페이지 입니다.')
    print('')

    save_pickle(urls, 'rnb_lyrics_link.pickle')


    
