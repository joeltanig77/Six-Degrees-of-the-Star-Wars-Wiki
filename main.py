from bs4 import BeautifulSoup  # Parsing HTML
import re  # Regular expressions
import requests  # Fetching pages
from collections import deque  # Free queue structure
import random


wikiFormat = "https://en.wikipedia.org"

def get_random_page_url():
    r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    return r.url


def internal_not_special(href):
    if href:
        if re.compile('^/wiki/').search(href):
            if not re.compile('/\w+:').search(href):
                if not re.compile('#').search(href):
                    return True
    return False

#For every link call it again


def findValidLinks(url):
    d = deque()
    url = requests.get(url)
    beautifulSoup = BeautifulSoup(url.text, 'html.parser')
    pageTitle = beautifulSoup.find("h1", id="firstHeading").string
    print(pageTitle)
    mainContent = beautifulSoup.find(id="bodyContent")
    # Let us now look for links
    linkLists = []
    validLinks = mainContent.find_all('a', href=internal_not_special)
    for i in range(len(validLinks)):
        tempLink = validLinks[i].get("href")
        finalLink = wikiFormat + tempLink
        if (finalLink == 'https://en.wikipedia.org/wiki/Star_Wars'):
            return
        if finalLink in linkLists:
            continue
        linkLists.append(finalLink)

    for i in range(len(linkLists)):
        print(linkLists[i])
        d.appendleft(linkLists[i])









def main():
    findValidLinks(get_random_page_url())
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
