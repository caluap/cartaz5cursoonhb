from PIL import Image
import numpy
img=Image.open('mapa-al-peq-peq.png')
imgarray=numpy.array(img)

c_la = []
c_world = []
c_sea = []

def gera_csv(nome, lista):
  text_file = open(nome, "w")
  s = ""
  for v in lista:
    s += "%s,%s\n" % (v[0],v[1])
  text_file.write("x,y\n%s" % s[:-1])
  text_file.close()


for y in range(len(imgarray)):
  for x in range(len(imgarray[y])):
    if imgarray[y][x][0] == 0:
      c_la.append((x+1,y+1))
    elif imgarray[y][x][0] == 128:
      c_world.append((x+1,y+1))
    else:
      c_sea.append((x+1,y+1))


gera_csv("c_la.csv", c_la)
gera_csv("c_world.csv", c_world)
gera_csv("c_sea.csv", c_sea)