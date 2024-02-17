import json

def lyricDataLoader():

    with open('data\\bal_lyrics_start.json', 'r', encoding='utf-8') as f:
        balladFirstLine = json.load(f)
    with open('data\\bal_lyrics_end.json', 'r', encoding='utf-8') as f:
        balladEndLine = json.load(f)
    with open('data\\rnb_lyrics_start.json', 'r', encoding='utf-8') as f:
        rnbFirstLine = json.load(f)
    with open('data\\rnb_lyrics_end.json', 'r', encoding='utf-8') as f:
        rnbEndLine = json.load(f)
    with open('data\\kkutuWords.json', 'r', encoding='utf-8') as f:
        kkutuWords = json.load(f)

    allLyricsData = balladFirstLine + balladEndLine + rnbFirstLine + rnbEndLine + kkutuWords

    return allLyricsData