from PIL import Image
import numpy
img=Image.open('mapa-al-peq-peq.png')
imgarray=numpy.array(img)

c_la = 0
c_world = 0
c_sea = 0
i = 0

s = ""

for row in imgarray:
  temp_s = ""
  for column in row:
    if column[0] == 0: 
      c_la += 1
      temp_s += "X,"
    elif column[0] == 128: 
      c_world += 1
      temp_s += "W,"
    else:
      c_sea += 1
      temp_s += "·,"
  
  s += temp_s[:-1] + "\n"

# print("la: %s \nworld: %s \nsea: %s" % (c_la,c_world,c_sea))
print(s)