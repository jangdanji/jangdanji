

import json
import requests
import pprint
import simplejson


LEAGUE_URL = 'https://overwatchleague.com/en-us/'
TRACK_URL = 'https://pk0yccosw3.execute-api.us-east-2.amazonaws.com/production/v2/sentinel-tracking/owl'
USERS_API_URL = 'https://playoverwatch.com/en-us/search/account-by-name/%s/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
HEADERS = {
    'accept-language': 'en-US,en;q=1.0',
    'origin': 'https://overwatchleague.com',
    'referer': 'https://overwatchleague.com/',
    'x-origin': 'overwatchleague.com',
    'user-agent': USER_AGENT
}


is_live = False

html = requests.get(LEAGUE_URL, headers=HEADERS).text

json_text = (
            html
            .split('<script id="__NEXT_DATA__" type="application/json">')[1]
            .split('</script>')[0]
        )

data = json.dumps(json_text, indent = 4, sort_keys = True)

# data_player = [i['videoPlayer'] for i in data['props']['pageProps']['blocks'] if i.get('videoPlayer')][0]

# pprint.pprint(data['props']['pageProps']['blocks'])

with open('C:\\Users\\NADANN\\Documents\\GitHub\\jonathan\\owl.json', 'w') as f:
	json.dump(data, f)

print(str(data))

exit()

was_live = is_live
entry_id = data_player['uid']

try:
    video_id = data_player['video']['id']
    is_live = bool(video_id)
except (KeyError, TypeError):
    video_id = None
    is_live = False

print(is_live)
print(video_id)