#coding: UTF-8
import kindleCheck
import tweet

url = "https://www.amazon.co.jp/gp/product/B06ZYMBXDG/ref=s9_acsd_al_bw_c_x_5_w?pf_rd_m=AN1VRQENFRJN5&pf_rd_s=merchandised-search-5&pf_rd_r=H6C9KK4T0MSYTF2K1TXN&pf_rd_r=H6C9KK4T0MSYTF2K1TXN&pf_rd_t=101&pf_rd_p=ab6f7325-aeea-4b12-8a6b-4e811e9cb73b&pf_rd_p=ab6f7325-aeea-4b12-8a6b-4e811e9cb73b&pf_rd_i=3338926051"
res = kindleCheck.getSaleInfo(url)

if res >= 30:
  tweet.tweet("セールだぞい" + url)

