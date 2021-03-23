from bs4 import BeautifulSoup   # Parsing HTML
import re                       # Regular expressions
import requests                 # Fetching pages
from collections import deque   # Queue structure


# Stores the path for each url
class Path:
    def __init__(self, url, list):
        self.url = url
        self.list = list


# Store start and end urls
class Storage:
    def __init__(self, url="", endURL=""):
        self.url = url
        self.endURL = endURL

    def setStartUrl(self, url):
        self.url = url

    def setEndURL(self, endURL):
        self.endURL = endURL

    def getStartUrl(self):
        return self.url

    def getENDURL(self):
        return self.endURL


title = ""
store = Storage()
wikiFormat = "https://en.wikipedia.org"


def get_random_page_url():
    r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    return r.url


def internal_not_special(href):
    # Check to make sure its a wiki link
    if href:
        if re.compile('^/wiki/').search(href):
            if not re.compile('/\w+:').search(href):
                if not re.compile('#').search(href):
                    return True
    return False


def findValidLinks(url):
    # Parse the html from the wiki page
    url = requests.get(url)
    beautifulSoup = BeautifulSoup(url.text, 'html.parser')
    mainContent = beautifulSoup.find(id="bodyContent")
    # Let us now look for links
    linkLists = []
    validLinks = mainContent.find_all('a', href=internal_not_special)
    for i in range(len(validLinks)):
        tempLink = validLinks[i].get("href")
        finalLink = wikiFormat + tempLink
        linkLists.append(finalLink)

    return linkLists


# Breadth first search the wiki pages
def bfs(vertex):
    q = deque()
    path = Path(vertex, [])
    path.list.append(vertex)
    q.appendleft(path)
    discovered = [vertex]
    print(f"Commencing Search for the {store.getENDURL()} wiki page\n")
    while q:
        popper = q.pop()
        print("Searching.... " + popper.url)
        url = popper.url
        linkLists = findValidLinks(url)
        if (len(popper.list) < 6):
            for i in range(len(linkLists)):
                if linkLists[i] not in discovered:
                    # Save the path
                    pathObj = Path(linkLists[i], None)
                    pathObj.list = popper.list + [linkLists[i]]
                    # If found, return and give us the path to our target
                    if (pathObj.url == store.getENDURL()):
                        return printPath(pathObj.list)

                    discovered.append(pathObj.url)
                    q.appendleft(pathObj)

    return didNotFind()


def printPath(path):
    print("\nFOUND!! Your fastest path to Star Wars is....")
    tab = ""
    for i in range(len(path)):
        url = requests.get(path[i])
        beautifulSoup = BeautifulSoup(url.text, 'html.parser')
        pageTitle = beautifulSoup.find("h1", id="firstHeading").string
        print(f"{tab}{pageTitle} ({path[i]})")
        tab += '\t'


def didNotFind():
    print(f"Could not find path from {store.getStartUrl()} to {store.getENDURL()} in 6 steps. Please try again")


def main():
    randURL = get_random_page_url()
    endURL = "https://en.wikipedia.org/wiki/Star_Wars"
    if randURL == endURL:
        print("You somehow got Star Wars as your Random Page, buy a lottery ticket or something!")
        exit(0)
    store.setEndURL(endURL)
    store.setStartUrl(randURL)
    bfs(randURL)


if __name__ == '__main__':
    main()
