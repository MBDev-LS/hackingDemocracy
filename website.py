
from bs4 import BeautifulSoup
import requests

from pprint import pprint
import re



BACKGROUND_PAGE_TITLES = ['campaign', 'news', 'press releases', 'newsletter'] # 'newsletter' is redundant because of 'news'

def search_link_list(linkList: list, searchWord: str) -> list:
	resultList = []
	# print(linkList)

	for linkElement in linkList:
		# print(searchWord, linkElement.text.lower())
		if searchWord in linkElement.text.lower():
			resultList.append(linkElement)
	
	return resultList

def get_unique_hrefs(linkList: list) -> set:
	hrefSet = set()

	for linkElement in linkList:
		hrefSet.add(linkElement['href'])
	
	return hrefSet


def extract_background_stories_from_page(url: str) -> list:
	pass

def get_base_url(url: str) -> str:
	results = re.findall(r'^(https?:\/\/([a-zA-Z0-9]|\.)+)', url)
	print(results)

	return results[0] if len(results) > 0 else None

print(get_base_url('https://www.jeremyhunt.org/'))


def get_background_stories_from_website(url: str) -> list:
	baseURL = 1

	try:
		html = requests.get(url)
	except:
		return []

	htmlSoup = BeautifulSoup(html.text, "html.parser")
	linkList = htmlSoup.find_all('a')

	uniqueHrefList = set()

	for searchWord in BACKGROUND_PAGE_TITLES:
		relevantLinks = search_link_list(linkList, searchWord)
		
		uniqueHrefList = uniqueHrefList.union( get_unique_hrefs(relevantLinks) )

	backgroundStoriesList = []

	# for href in 1:
	print(uniqueHrefList)



get_background_stories_from_website('https://www.jeremyhunt.org/')