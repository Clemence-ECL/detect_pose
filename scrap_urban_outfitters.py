from bs4 import BeautifulSoup
import os
import urllib.request

url = "https://www.urbanoutfitters.com/fr-fr/blouses-shirts"

def get_urls_pages(url):
  liste = []
  response = urllib.request.urlopen(url)
  soup = BeautifulSoup(response,'lxml')
  for link in soup.find_all('a',class_='c-product-tile__image-link'):
    liste += ['https://www.urbanoutfitters.com'+link.get('href')]
  return liste

def down_images(url):
  liste = get_urls_pages(url)
  for url in liste :
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,'lxml')
    for img in soup.find_all('img',class_='o-slider--product-image'):
      link_deb = img.get('src')[:-17]
      link_fin = img.get('src')[-14:]
      nom = img.get('src').split('?')[0].split('/')[6]
      print('https:'+link_deb+'900'+link_fin)
      urllib.request.urlretrieve('https:'+link_deb+'900'+link_fin,'images/UO-'+nom+'-chemise')

down_images(url)
# https://euimages.urbanoutfitters.com/is/image/UrbanOutfittersEU/5112477797158_012_g?$xlarge$&amp;hei=150&amp;fit=constrain
