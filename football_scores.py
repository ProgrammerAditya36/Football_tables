import requests
from tabulate import tabulate
import json
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()
competitions = []
uri = 'https://api.football-data.org/v4/competitions/'
headers = {'X-Auth-Token': os.getenv('api_key')}

response = requests.get(uri, headers=headers)
data = response.json()['competitions']

for comp in data:
    competitions.append({'name': comp['name'], 'code': comp['code']})
choice = 0
while choice != len(competitions) + 1:
    for i in range(len(competitions)):
        if i != 12:
            print(f"{i + 1}.{competitions[i]['name']}")
    choice = int(input(f"{len(competitions) + 1}.Exit\nChoose:-"))
    if choice == len(competitions) + 1:
        break
    uri = f"https://api.football-data.org/v4/competitions/{competitions[choice - 1]['code']}/standings"
    r = requests.get(url=uri, headers=headers).json()
    d = r['standings']
    for i in range(len(d)):
        table = []
        for team in d[i]['table']:
            table.append(
                {'Position': team['position'], 'Name': team['team']['name'], 'Games Played': team['playedGames'],
                 'Wins': team['won'], 'Lost': team['lost'], 'Draw': team['draw'], 'Points': team['points'],
                 'GF': team['goalsFor'], 'GA': team['goalsAgainst'], 'GD': team['goalDifference']})
        print(tabulate(table, headers="keys", tablefmt="outline", colalign=("center",)))
