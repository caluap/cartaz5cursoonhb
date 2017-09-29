from PIL import Image
import numpy
img=Image.open('mapa-al-peq-peq.png')
imgarray=numpy.array(img)

c_la = 0
c_world = 0
c_sea = 0
i = 0

s = ""

header = ""

for row in imgarray:
  if header == "":
    for i_h in range(len(row)):
      header += "C" + str(i_h) + ","
  temp_s = ""
  for column in row:
    if column[0] == 0: 
      c_la += 1
      temp_s += "10,"
    elif column[0] == 128: 
      c_world += 1
      temp_s += "4,"
    else:
      c_sea += 1
      temp_s += "0,"
  
  s += temp_s[:-1] + "\n"

# print("la: %s \nworld: %s \nsea: %s" % (c_la,c_world,c_sea))
print(header[:-1])
print(s[:-1])

text_file = open("mapa.csv", "w")
text_file.write("%s\n%s" % (header[:-1], s[:-1]))
# text_file.write(s[:-1])
text_file.close()
