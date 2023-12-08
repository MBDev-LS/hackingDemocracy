
from bs4 import BeautifulSoup
import requests

from pprint import pprint
import re


BACKGROUND_PAGE_TITLES = ['campaign', 'news', 'press releases', 'newsletter'] # 'newsletter' is redundant because of 'news'
BASE_URL_REGEX = r'^(https?:\/\/([a-zA-Z0-9]|\.)+)'


def get_base_url(url: str) -> str:
	results = re.findall(BASE_URL_REGEX, url)
	print(results)

	return results[0][0] if len(results) > 0 else None


def search_link_list(linkList: list, searchWord: str) -> list:
	resultList = []

	for linkElement in linkList:
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


def get_background_stories_from_website(url: str) -> list:
	baseUrl = get_base_url(url)

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
	validUrlList = [baseUrl + hrefStr.replace(baseUrl, '') for hrefStr in uniqueHrefList]
	
	for validUrl in validUrlList:
		backgroundStoriesList += extract_background_stories_from_page(validUrl)
	
	return backgroundStoriesList


get_background_stories_from_website('https://www.jeremyhunt.org/')
