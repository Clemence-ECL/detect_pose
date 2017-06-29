import os
import os.path
import sys
import dryscrape
# from bs4 import BeautifulSoup
import urllib
import urllib.request
import random
import requests
# from requests.auth import HTTPProxyAuth
import csv


if 'linux' in sys.platform:
  dryscrape.start_xvfb()


# __PROXY_AUTH = HTTPProxyAuth('4528a6fcc4ee45ba9f5d39ade1f24037', '')
# __PROXIES = {'https': 'https://proxy.crawlera.com:8010/', 'http': 'http://proxy.crawlera.com:8010/'}
# __CACERT = os.path.join(os.getcwd(), 'crawlera-ca.crt')

# def __request(url):
#     return requests.get(
#         url,
#         proxies=__PROXIES,
#         auth=__PROXY_AUTH,
#         verify=__CACERT
#     )


# def download_image(url, path):
#   response = __request(url)
#   if response.status_code == 200:
#       with open(path, 'wb') as f:
#           f.write(response.content)


def verify_path(path):
  if os.path.exists(path) is False :
    os.makedirs(path)

cr = csv.reader(open('data_showroom_with_links_no_duplicate_2.csv','r'))
categories = csv.reader(open('categories_showroom.csv','r'))

# Creation de la liste des categories
liste_cat = []
for category in categories:
  liste_cat += category

#Place into files
indent = 0
for row in cr:

  folder_face = 'images/face'
  folder_back = 'images/back'
  folder_full = 'images/full'
  folder_zoom = 'images/zoom'

  if row[0]=='Vp_id':
    next
  else:
    if row[4].split(' ')[0] in liste_cat :
      nameImage = row[1].split(' ')[0]+'-'+row[2]+'-'+row[4].split(' ')[0]+'.jpg'
      if row[9]!='':
        next
      else:
        try :
          nom_face = os.path.join(folder_face,nameImage)
          urllib.request.urlretrieve(row[5],nom_face)
          nom_back = os.path.join(folder_back, nameImage)
          urllib.request.urlretrieve(row[6],nom_back)
          nom_full = os.path.join(folder_full,nameImage)
          urllib.request.urlretrieve(row[7],nom_full)
          nom_zoom = os.path.join(folder_zoom,nameImage)
          urllib.request.urlretrieve(row[8],nom_zoom)
        except ValueError:
          pass
  indent += 1
  if indent%200 == 0 :
    input("Press enter to continue...")










# def class_into_folders():
#   repartition = ['train']*80+['validation']*10
#   indent = 0
#   cr = csv.reader(open('table_final.csv','r'))
#   folder_train = 'images_nuji/train'
#   folder_validation = 'images_nuji/validation'
#   for row in cr :
#     if row == ['Marque','Genre','Catégorie','Nom','Prix','Description','Lien Revendeur','Lien image']:
#       next
#     else :
#       link_to_img = row[7]
#       category = row[2]
#       nameImage = category+str(indent)
#       place = random.choice(repartition)
#       if place == 'train' :
#         folder = folder_train+'/'+category
#         verify_path(folder)
#         nom = os.path.join(folder,nameImage)
#         download_image(link_to_img,nom)
#       elif place=='validation':
#         folder = folder_validation+'/'+category
#         verify_path(folder)
#         nom = os.path.join(folder,nameImage)
#         download_image(link_to_img,nom)
#       indent += 1

# class_into_folders()
