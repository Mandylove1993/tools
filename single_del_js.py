import json
import cv2


json_filename='/home/zft/chenxu/val/0009.json' 
txt_filename = '/home/zft/chenxu/val/final.txt'
img = cv2.imread('/home/zft/chenxu/c.png')
sp = img.shape

root = json.load(open(json_filename))
size1 = len(root['children'])
W = sp[1]
H = sp[0]

xmax = []
xmin = []
ymax = []
ymin = []
name = []
bx = []
by = []
bw = []
bh = []

for i in range(size1):
    xb = root["children"][i]["maxcol"]
    #xmax.append(xb)
    xa = root["children"][i]["mincol"]
    #xmin.append(xa)
    yb = root["children"][i]["maxrow"]
    #ymax.append(yb)
    ya = root["children"][i]["minrow"]
    #ymin.append(ya)
    sin_name = root["children"][i]["identity"]
    if (str(sin_name) == 'mopedrider' or sin_name == 'cyclist' or sin_name == 'motorcyclist'):
        name.append(sin_name)
        xmax.append(xb)
        xmin.append(xa)
        ymax.append(yb)
        ymin.append(ya)
    else:
        continue
file = open(txt_filename,'w') 
size2 = len(name)
for index in range(size2):
    x = (xmax[index]+xmin[index])/2/W
    bx.append(x)
    y = (ymax[index]+ymin[index])/2/H
    by.append(y)
    w = (xmax[index]-xmin[index])/W
    bw.append(w)
    h = (ymax[index]-ymin[index])/H
    bh.append(h)
    temp = name[index] + ' ' + str(bx[index]) + ' ' +str(by[index]) + ' '+ str(bw[index]) + ' ' + str(bh[index])
    file.write(temp + '\n')

file.close()



  
    

