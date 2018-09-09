# -*- coding: utf-8 -*-
import os
import shutil

oldimg_path = '/home/zft/chenxu/images/tdcb_test/'
newimg_path = '/home/zft/chenxu/images/my_tdcb_test/'
label_path = '/home/zft/chenxu/my_labels/my_tdcb_test/'

filelist = os.listdir(label_path)
for file in filelist:
    filename = os.path.split(file)[-1].split('.')[0] #get image name
    shutil.copy(os.path.join(oldimg_path + filename +'.png'),os.path.join(newimg_path + filename + '.png'))
    print(filename+ '.png has moved !')
