from bs4 import BeautifulSoup
import requests
import re

# TODO: if missed retry 3 seconds later.
def getSaleInfo(url):
  h = requests.get(url).text
  sp = BeautifulSoup(h, "html.parser")
  tr = sp.find("tr", class_="kindle-price")
  if tr is not None:
    if tr.p is not None and tr.p.text is not None:
      pattern = "\(([0-9]+)%\)"
      mc = re.search(pattern, tr.p.text)
      return int(mc.group(1))
    else:
      return 0
  else:
    return -1

