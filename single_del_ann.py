#coding=utf-8
import os
import os.path
import xml.etree.ElementTree as ET

file = '/home/zft/chenxu/2007_000123.xml'
tree = ET.parse('/home/zft/chenxu/2007_000123.xml')
root = tree.getroot()

for object in root.findall('object'):
    name = str(object.find('name').text)
    if (name != 'bicycle' and name!= 'person' and name!= 'bus' and name!= "car" and name!= 'motorbike'):
        root.remove(object)
      
      
tree.write('output.xml')

