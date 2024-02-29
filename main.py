import os
import requests
import argparse

parser = argparse.ArgumentParser(
                    prog='Radio Garden M3U Generator',
                    description='This script generates a M3U file with stations from Radio Garden.')

parser.add_argument('--country', help='Country name', type=str, required=True)
parser.add_argument('--state', help='State or province name', type=str, required=False)
args = parser.parse_args()


BASE_URL = "http://radio.garden/api"

def get_places():
    
    list = []
    
    data = requests.get(f"{BASE_URL}/ara/content/places").json()['data']['list']
    for place in data:
        list.append([place['country'], # Country
                     place['title'], # City, State or Province
                     place['id']]) # Place ID

    return sorted(list)

def get_stations(place_id):
        list = []
        
        data = requests.get(f"{BASE_URL}/ara/content/page/{place_id}/channels").json()['data']['content'][0]['items']
        for station in data:
            list.append([station['page']['title'], # Station Name
                        station['page']['url'].split("/")[-1]]) # Station ID    
        return list
    
def get_stream_url(station_id):
    return f"{BASE_URL}/ara/content/listen/{station_id}/channel.mp3"


def m3u(stations):
    f = open('radio.m3u','a', encoding='utf-8')  

    # if the file is empty, write the header
    if os.path.getsize("radio.m3u") == 0:
        f.write('#EXTM3U\n')

    for station in stations:
        station_name = station[0]
        stream_url = get_stream_url(station[1])
        f.write(f'#EXTINF:-1 tvg-name="{station_name}", {station_name}\n')
        f.write(f'{stream_url}\n')
    f.close()

def main():
    open('radio.m3u', 'w').close()
    if not args.state:
        places = get_places()
        for place in places:
            if args.country in place[0]:
                print(place[1])
                stations = get_stations(place[2])
                m3u(stations)
    if args.state:
        places = get_places()
        for place in places:
            if args.state in place[1]:
                print(place[1])
                stations = get_stations(place[2])
                m3u(stations)

if __name__ == "__main__":
    main()