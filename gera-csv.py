from PIL import Image
import numpy
img=Image.open('mapa-al-peq.png')
imgarray=numpy.array(img)

c_la = 0
c_world = 0
c_sea = 0
i = 0

for row in imgarray:
  for column in row:
    for value in column:
      if value == 0: 
        c_la += 1
      if value == 128: 
        c_world += 1
      if value == 255: 
        c_sea += 1
      i += 1
      print(i)

print("la: %s \nworld: %s \nsea: %s" % (c_la,c_world,c_sea))