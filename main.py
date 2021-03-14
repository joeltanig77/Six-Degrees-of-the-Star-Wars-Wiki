from bs4 import BeautifulSoup #Parsing HTML
import re #Regular expressions
import requests #Fetching pages
from collections import deque #Free queue structure



def get_random_page_url():
    r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    return r.url


def internal_not_special(href):
    if href:
        if re.compile('ˆ/wiki/').search(href):
            if not re.compile('/\w+:').search(href):
                if not re.compile('#').search(href):
                    return True
    return False

def skimPage():
    url = requests.get(get_random_page_url())
    beautifulSoup = BeautifulSoup(url.text,'html.parser')
    pageTitle = beautifulSoup.find("h1", id="firstHeading").string
    print(pageTitle)
    mainContent = beautifulSoup.find(id="bodyContent")
    #Let us now look for links
    #print(mainContent)
    findValidLinks(mainContent)



def findValidLinks(mainContent):
    validLinks = mainContent.find_all('a', href=internal_not_special)
    print(validLinks)


def main():
    skimPage()
    return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
