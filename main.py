from bs4 import BeautifulSoup  # Parsing HTML
import re  # Regular expressions
import requests  # Fetching pages
from collections import deque  # Free queue structure




wikiFormat = "https://en.wikipedia.org"

def get_random_page_url():
    r = requests.get('https://en.wikipedia.org/wiki/George_Lucas')
    return r.url
#https://en.wikipedia.org/wiki/Special:Random'

def internal_not_special(href):
    if href:
        if re.compile('^/wiki/').search(href):
            if not re.compile('/\w+:').search(href):
                if not re.compile('#').search(href):
                    return True
    return False

#For every link call it again


def findValidLinks(url):
    url = requests.get(url)
    beautifulSoup = BeautifulSoup(url.text, 'html.parser')
    pageTitle = beautifulSoup.find("h1", id="firstHeading").string
    print(pageTitle)
    mainContent = beautifulSoup.find(id="bodyContent")
    # Let us now look for links
    linkLists = []
    finalLink = ""
    validLinks = mainContent.find_all('a', href=internal_not_special)
    for i in range(len(validLinks)):
        tempLink = validLinks[i].get("href")
        finalLink = wikiFormat + tempLink

        if finalLink in linkLists:
            continue
        linkLists.append(finalLink)

   # for i in range(len(linkLists)):
       # print(linkLists[i])

    return linkLists





def bfs(vertex):
    q = deque()
    path = deque()
    q.appendleft(vertex)
    discovered = []
    while q:
        vertex = q.pop()
        if vertex == 'https://en.wikipedia.org/wiki/Star_Wars':
            return "FOUNDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
        linkLists = findValidLinks(vertex)
        for i in range(len(linkLists)):
            if linkLists[i] not in discovered:
                print(linkLists[i])
                if (linkLists[i] == 'https://en.wikipedia.org/wiki/Star_Wars'):
                    return
                discovered.append(linkLists[i])
                q.appendleft(linkLists[i])



def printPath(path):
    print(f"The final link is {path}")
    exit(0)


def main():
    randURL= get_random_page_url()
    #print(dictLinks)
    bfs(randURL)
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
