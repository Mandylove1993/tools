#coding=utf-8
import os
import os.path
import xml.etree.ElementTree as ET
 
path="/home/zft/chenxu/test/"
files=os.listdir(path)  #得到文件夹下所有文件名称


for xmlFile in files: #遍历文件夹
    tree = ET.parse(os.path.join(path,xmlFile))
    #tree = ET.parse('/home/zft/chenxu/2007_000346.xml')
    root = tree.getroot()
    for object in root.findall('object'):
        name = str(object.find('name').text)
        if (name != 'bicycle' and name!= 'person' and name!= 'bus' and name!= "car" and name!= 'motorbike'):
            root.remove(object)
    tree.write(os.path.join(path,xmlFile))

    new_tree = ET.parse(os.path.join(path,xmlFile))
    new_root = new_tree.getroot()
    count=0
    for obj in  new_root.iter('object'): 
        count+=1  
    if count==0:
        print(os.path.basename(xmlFile))
      
print('OK!')

