#!/usr/bin/env python
# coding=utf-8
import json
from xml.dom.minidom import Document

src = open("/home/zft/chenxu/val/c.json")
obj = json.loads(src.read())

doc = Document()

def traverse_data(json_data,preNode = None):
    # 创建根节点
    if isinstance(json_data,dict):
        dict_data= {}
        #获取所有的key值
        keys = json_data.keys()
        node = doc.createElement("node")
        for var in keys:
            if var != "children":
                node.setAttribute(str(var), str(json_data[var]))
        if preNode != None:
            preNode.appendChild(node)
        else:
            doc.appendChild(node)
        # 创建根元素
        if json_data.get("children") != None:
            traverse_data(json_data.get("children"),node)

    elif isinstance(json_data,list):
        for element in json_data:
            if element != None and len(element) > 0:
                if isinstance(element,dict):
                    dict_data1 = {}
                    # 获取所有的key值
                    keys1 = element.keys()
                    node = doc.createElement("node")
                    for var1 in keys1:
                        if var1 != "children":
                            print (element[var1])
                            node.setAttribute(str(var1),str(element[var1]))
                    if preNode != None:
                        preNode.appendChild(node)
                    else:
                        doc.appendChild(node)
                    if  element.get("children") != None:
                        traverse_data(element.get("children"),node)


fp = open("./xml.xml", 'w')
traverse_data(obj)