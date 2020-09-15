# Bu araç @Hilas tarafından | @KekikAkademi için yazılmıştır.


import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/emtialar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

baslik = soup.find("span", {"class":"page-title"}).text
print(baslik)
print("-" * 15)
print("")

name = soup.find("tbody").find_all("tr")

for i in range(0, 5):
  emtiaName = name[i].find("a").text
  sonFiyat = name[i].find("td", {"class":"text-bold"}).text
  enDusuk = name[i].select("td:nth-child(3)")[0].text
  enYuksek = name[i].select("td:nth-child(4)")[0].text
  degisim = name[i].find_all("td")[4].text.strip()
  

  print("Emtia İsmi: {}".format(emtiaName))
  print("Son Değer: {}".format(sonFiyat))
  print("En Düşük Değer: {}".format(enDusuk))
  print("En Yüksek Değer: {}".format(enYuksek))
  print("Değişim: {}".format(degisim))
  print("-" * 25)