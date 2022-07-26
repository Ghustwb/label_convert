#转换数据集为PascalVoc格式
#标注坐标为图片的文件名
#
#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import cv2
sys.path.append("C:\\Users\\Carpenter\\Desktop\\label_convert")
dir_name = os.path.abspath(os.path.dirname(__file__))
libs_path = os.path.join(dir_name, '..', 'libs')
sys.path.insert(0, libs_path)
sys.path.insert(0, dir_name)
from pascal_voc_io import PascalVocWriter
from pascal_voc_io import PascalVocReader

from numpy import linspace



def getW_H_C(pic_path):
    img = cv2.imread(pic_path)
    if(img is None):
        print("img is None")
        return 0,0,0
    return img.shape[0], img.shape[1],img.shape[2]

def main():
    xml_folder = r"C:\Users\Carpenter\Downloads\绿牌数据集-1\xml"
    img_folder = r"C:\Users\Carpenter\Downloads\绿牌数据集-1\新能源车牌_[1250张]"
    for file in os.listdir(img_folder):
        if (file.endswith(".jpg") or file.endswith(".JPG")):
            index1 = file.find("[")
            index2 = file.find("]")
            pos_str = file[index1+1:index2]
            print("str: ",pos_str)
            pos_values = pos_str.split(".")
            x1 = pos_values[0]
            y1 = pos_values[2]
            x2 = pos_values[1]
            y2 = pos_values[3]
            img_file = os.path.join(img_folder, file)
            xml_file = os.path.join(xml_folder, file[0:-4] + ".xml")
            objs = []
            objs.append((x1, y1, x2, y2, 'Licenseplate',1))
            print("img: ",img_file)
            print("obj: ",objs[0])
            w,h,c = getW_H_C(img_file)
            writer = PascalVocWriter('dir', 'path',(w,h,c) , img_file)
            # img = cv2.imread(img_file)
            # cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            # cv2.imshow("img", img)
            # cv2.waitKey(0)
            for obj in objs:
                writer.add_bnd_box(int(obj[0]), int(obj[1]), int(obj[2]), int(obj[3]), obj[4], obj[5])
            writer.save(xml_file)
            print(xml_file,"OK")
            

if __name__ == '__main__':
    main()
