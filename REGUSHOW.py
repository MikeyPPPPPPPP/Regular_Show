import wget
import requests
from bs4 import BeautifulSoup
import re


class regshow:
    def __init__(self):
        self.url = 'http://www.animetoon.org/regular-show'
        self.pages = []
        self.links = []
        self.soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        for x in self.soup.find_all('button'):
            try:
                self.pages.append(x['href'])
            except:
                pass

    def get_links(self, site):
        soups = BeautifulSoup(requests.get(site).text, 'html.parser')
        for x in soups.find_all('a'):
            if self.url in x['href']:
                self.links.append(x['href'])

    def downloader(self):
        for links in self.links:
            vidurls = []
            soup = BeautifulSoup(requests.get(links).text, 'html.parser')
            for x in soup.find_all('iframe'):
                try:
                    vidurls.append(x['src'])
                except:
                    pass

            soups = BeautifulSoup(requests.get(vidurls[0]).text, 'html.parser')

            u = re.findall("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", requests.get(vidurls[0]).text)[-1]
            good = ''.join(u).replace('http', 'http://')
            wget.download(good)


a = regshow()
for x in a.pages:
    a.get_links(x)

a.downloader()



