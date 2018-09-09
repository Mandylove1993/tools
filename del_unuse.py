import os
import os.path


file_label = "/home/zft/chenxu/labels/"
files = os.listdir(file_label)

file_txt = "/home/zft/chenxu/unuse.txt"
lines = open(file_txt).readlines()

''''for line in lines:
    del_name = line.split('.')[0]
    for file in files:
        filename = os.path.split(file)[-1].split('.')[0]
        if str(filename) == str(del_name):
            os.remove(os.path.join(file_label,file))
            print("%s has removed!"%filename)
'''
for line in lines:
    del_name = line.split('.')[0]
    os.remove(os.path.join(file_label + del_name + '.txt'))
        