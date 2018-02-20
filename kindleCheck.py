import urllib2
from bs4 import BeautifulSoup
import re

# 30%以上がセール
# 29%以下なら0を返す
# 割引率を取得できなかったら-1を返す
# TODO: Error 503
def getSaleInfo(url):
  h = urllib2.urlopen(url)
  sp = BeautifulSoup(h, "html.parser")
  tr = sp.find("tr", class_="kindle-price")
  if tr is not None:
    txt = tr.p.text
    pattern = "\(([0-9]+)%\)"
    mc = re.search(pattern, txt)
    if int(mc.group(1)) >= 30:
      print "Sale!!"
      return int(mc.group(1))
    else:
      print "no sale..."
      return 0
  else:
    print "miss"
    return -1

#getSaleInfo("https://www.amazon.co.jp/%E3%82%B4%E3%83%BC%E3%83%AB%E3%83%87%E3%83%B3%E3%82%AB%E3%83%A0%E3%82%A4-12-%E3%83%A4%E3%83%B3%E3%82%B0%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%97%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%82%B9DIGITAL-%E9%87%8E%E7%94%B0%E3%82%B5%E3%83%88%E3%83%AB-ebook/dp/B077JRKQSX/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=")
#getSaleInfo("https://www.amazon.co.jp/kindle-dbs/manga-store/ref=sv_kinc_3?_encoding=UTF8&node=2293143051")
