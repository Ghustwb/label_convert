#转换CPRD数据集为PascalVoc格式
#
#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import cv2

dir_name = os.path.abspath(os.path.dirname(__file__))
libs_path = os.path.join(dir_name, '..', 'libs')
sys.path.insert(0, libs_path)
from pascal_voc_io import PascalVocWriter
from pascal_voc_io import PascalVocReader

from numpy import linspace


#read lines from txt file
def readTxt(txt_file):
    with open(txt_file, "r") as file:
        lines = file.readlines()
    objList = []
    for line in lines:
        xmin = line.split(' ')[0]
        ymin = line.split(' ')[1]
        xmax = line.split(' ')[4]
        ymax = line.split(' ')[5]
        objList.append((xmin, ymin, xmax, ymax, 'Licenseplate',1))#[xmin,ymin,xmax,ymax,label,difficult]
    return objList

def getW_H_C(pic_path):
    img = cv2.imread(pic_path)
    return img.shape[0], img.shape[1],img.shape[2]

def main():
    txt_folder = "/home/lcg/Downloads/CRPD_all/all/txt"
    xml_folder = "/home/lcg/Downloads/CRPD_all/all/xml"
    img_folder = "/home/lcg/Downloads/CRPD_all/all/img"
    for file in os.listdir(txt_folder):
        if file.endswith(".txt"):
            file_name = file.split(".")[0]
            txt_file = os.path.join(txt_folder, file)
            img_file = os.path.join(img_folder, file_name + ".jpg")
            xml_file = os.path.join(xml_folder, file_name + ".xml")
            objs = readTxt(txt_file)
            print(img_file)
            w,h,c = getW_H_C(img_file)
            writer = PascalVocWriter('dir', 'path',(w,h,c) , img_file)
            for obj in objs:
                writer.add_bnd_box(int(obj[0]), int(obj[1]), int(obj[2]), int(obj[3]), obj[4], obj[5])
            writer.save(xml_file)
            print(xml_file,"OK")
            

if __name__ == '__main__':
    main()
