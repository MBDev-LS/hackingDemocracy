
import pywikibot

site = pywikibot.Site('wikidata')
pages = site.search('Diane Abbott')



print(pages)

# page = pywikibot.Page(site, 'Diane Abbott')

# print(page.full_url())