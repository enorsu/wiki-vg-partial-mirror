import re
from bs4 import BeautifulSoup
import os

def getLinks():
    with open("a.html", "r") as f: f = f.read()

    soup = BeautifulSoup(f , 'html.parser')
    links = []
    for link in soup.find_all("a"):
        ap = str(link.get("href"))
        if ap.startswith("/w/"):
            links.append(link.get("href"))
    return links


def DL():

    links = getLinks()

    for x in links:
        url = "https://minecraft.wiki" + x
        command = "wget -P ./wikivg " + url
        print(">" + command)
        os.system(command)

DL()