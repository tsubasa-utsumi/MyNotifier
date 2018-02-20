from bs4 import BeautifulSoup
import requests
import re

# TODO: if missed retry 3 seconds later.
def getSaleInfo(url):
  h = requests.get(url).text
  sp = BeautifulSoup(h, "html.parser")
  tr = sp.find("tr", class_="kindle-price")
  if tr is not None:
    txt = tr.p.text
    pattern = "\(([0-9]+)%\)"
    mc = re.search(pattern, txt)
    return int(mc.group(1))
  else:
    return -1

