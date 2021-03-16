from bs4 import BeautifulSoup  # Parsing HTML
import re  # Regular expressions
import requests  # Fetching pages
from collections import deque  # Queue structure


wikiFormat = "https://en.wikipedia.org"

class Path:
    def __init__(self,url,list):
        self.url = url
        self.list = list




def get_random_page_url():
    r = requests.get('https://en.wikipedia.org/wiki/Manga')
    return r.url
#https://en.wikipedia.org/wiki/Special:Random'
#https://en.wikipedia.org/wiki/George_Lucas


def internal_not_special(href):
    if href:
        if re.compile('^/wiki/').search(href):
            if not re.compile('/\w+:').search(href):
                if not re.compile('#').search(href):
                    return True
    return False


def findValidLinks(url):
    url = requests.get(url)
    beautifulSoup = BeautifulSoup(url.text, 'html.parser')
    pageTitle = beautifulSoup.find("h1", id="firstHeading").string
    mainContent = beautifulSoup.find(id="bodyContent")
    # Let us now look for links
    linkLists = []
    validLinks = mainContent.find_all('a', href=internal_not_special)
    for i in range(len(validLinks)):
        tempLink = validLinks[i].get("href")
        finalLink = wikiFormat + tempLink
        #print(finalLink)
        linkLists.append(finalLink)

    return linkLists


def bfs(vertex):
    q = deque()
    path = Path(vertex, [])
    path.list.append(vertex)
    q.appendleft(path)
    discovered = [vertex]
    while q:
        popper = q.pop()
        print("Searching.... " + popper.url)
        url = popper.url
        #print(vertex.list)
        linkLists = findValidLinks(url)
        #print(len(popper.list))
        #Check that we only go for 6 depth here
        if (len(popper.list) < 6):
            #print(len(linkLists))
            for i in range(len(linkLists)):
                #print(vertex.url)
                if linkLists[i] not in discovered:
                    #print(linkLists[i])
                    #print(linkLists[i])
                    pathObj = Path(linkLists[i], None)
                    pathObj.list = popper.list + [linkLists[i]]
                    #print(pathObj.list)
                    if (pathObj.url == 'https://en.wikipedia.org/wiki/Star_Wars'):
                        return printPath(pathObj.list)

                    discovered.append(pathObj.url)
                    q.appendleft(pathObj)

    return didNotFinish()


def printPath(path):
    print(f"The final Path is {path}")


def didNotFinish():
    print("Could not find path to wiki page in 6 steps")


def main():
    randURL= get_random_page_url()
    bfs(randURL)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
