
import config

from pathlib import Path
import csv
import json
import requests

from pprint import pprint

BASE_DIR = Path(config.BASE_DIR)
RESOURCE_DIR = BASE_DIR / 'resources'


def flatternList(lst: list) -> list:
	flatList = []
	
	for item in lst:
		flatList += item
	
	return flatList


# with open(RESOURCE_DIR / 'party_list.json') as party_file:
#     jsonPartyDir = json.loads(party_file.read())


# for partyInfoDict in jsonPartyDir['items']:
#     partyInfo = partyInfoDict['value']['party']

#     print(partyInfo['name'], partyInfoDict['value']['total'], round(partyInfoDict['value']['total'] / 650 * 100))



# partyDict = {}




# with open(RESOURCE_DIR / 'mp_list.csv') as mps_file:
#     csv_reader = csv.reader(mps_file, delimiter=',')

#     for mpRow in csv_reader:
#         if mpRow[3] not in partyDict:
#             partyDict[mpRow[3]] = []
		
#         partyDict[mpRow[3]].append(mpRow)

# pprint(partyDict)


with open(RESOURCE_DIR / 'sample.json') as sample_json:
	sampleDict = json.loads(sample_json.read())


mpSampleList = flatternList([sampleDict[key] for key in sampleDict])
mpDictSampleList = []

for constituencyName in mpSampleList:
	responseJson = requests.get(f'https://members-api.parliament.uk/api/Location/Constituency/Search?searchText={constituencyName}&skip=0&take=1').json()
	pprint(responseJson)
	mpDictSampleList.append({
		'name': responseJson['items'][0]['value']['currentRepresentation']['member']['value']['nameDisplayAs'],
		'id': responseJson['items'][0]['value']['currentRepresentation']['member']['value']['id'],
	})

pprint(mpDictSampleList)