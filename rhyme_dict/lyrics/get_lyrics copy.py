import chrome
import glob
import pickle

def save_pickle(urls, name):
    # with open(f"C:\\Users\\01271\\Documents\\Github\\jonathan\\rhyme_dict\\lyrics\\{name}.pickle", 'wb') as f:
    with open(f"rhyme_dict\\lyrics\\{name}.pickle", 'wb') as f:
    # with open("C:\\Users\\NADANN\\Documents\\jonathan\\rhyme_dict\\lyrics\\lyrics_links.pickle", 'wb') as f:
        pickle.dump(name, f, pickle.HIGHEST_PROTOCOL)

ret = glob.glob(f'rhyme_dict\\lyrics\\rnb_lyrics_link.pickle')
with open(ret[0], 'rb') as f: rnb_link = pickle.load(f)

ret = glob.glob(f'rhyme_dict\\lyrics\\ballad*')
with open(ret[0], 'rb') as f: ballad_link = pickle.load(f)

print(ballad_link)

    
