import os

directory = 'data/validation/no_extension'
images = os.listdir(directory)

#defaire l'erreur
# for img in images :
#   if os.path.isdir(img):
#     next
#   else:
#     if img[-3:]=='.jpg':
#       next
#     else:
#       path = os.path.join(directory,img)
#       target = os.path.join(directory, img[:-4])
#       os.rename(path, target)


for img in images :
  if os.path.isdir(img):
    next
  else:
    path = os.path.join(directory,img)
    target = os.path.join(directory,img+'.jpg')
    os.rename(path, target)
