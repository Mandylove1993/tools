import json
import cv2
import os
import os.path



#获取文件夹中的所有要转换的json文件
path_inport = "/home/zft/chenxu/val/"
path_image = "/home/zft/chenxu/images/"
files = os.listdir(path_inport) 
#获取保存文件的地址
path_outport = "/home/zft/chenxu/labels/"

for jsonFile in files:
    Filepath = path_inport + jsonFile
    root = json.load(open(Filepath))
    size1 = len(root['children']) #获取该属性包含目标个数
    filename = os.path.split(jsonFile)[-1].split('.')[0]#获取文件名
    imagename = str(filename).replace("labelData","leftImg8bit")
    image = os.path.join(path_image + imagename + '.png') #获取图片路径
    print (image)
    img = cv2.imread(image)#获取图片大小
    sp = img.shape
    W = sp[1]
    H = sp[0]
    #设置对象数组
    xmax = []
    xmin = []
    ymax = []
    ymin = []
    name = []
    bx = []
    by = []
    bw = []
    bh = []
    #将对应的对象数据加入到数组
    for i in range(size1):
        xb = root["children"][i]["maxcol"]
        xa = root["children"][i]["mincol"]
        yb = root["children"][i]["maxrow"]
        ya = root["children"][i]["minrow"]
        sin_name = root["children"][i]["identity"]
        #筛选要的标签进行保存
        if (str(sin_name) == 'mopedrider' or sin_name == 'cyclist' or sin_name == 'motorcyclist'):
            name.append(sin_name)
            xmax.append(xb)
            xmin.append(xa)
            ymax.append(yb)
            ymin.append(ya)
        else:
            continue
    #计算中心坐标x,y和w，h的值并存入数组
    file = open(os.path.join(path_outport + filename + '.txt'),'w')
    #重新获取数组长度
    size2 = len(name)
    file2 = open("home/zft/chenxu/tdcbunuse.txt",'W')
    if size2 == 0:
        print (filename)
    else:
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

