#将CPPD格式转换数据集为PascalVoc格式
#标注坐标为图片的文件名
'''
样本图像名称为“ 025-95_113-154&383_386&473-386&473_177&454_154&383_363&402-0_0_22_27_27_33_16-37-15.jpg”。
每个名称可以分为七个字段，以-符号作为分割。这些字段解释如下。

面积：车牌面积与整个图片区域的面积比。025 (25%)

倾斜度：水平倾斜程度和垂直倾斜度。水平 95度 垂直 113度

边界框坐标：左上和右下顶点的坐标。左上(154,383) 右下(386,473)

四个顶点位置：整个图像中车牌的四个顶点的精确（x，y）坐标。这些坐标从右下角顶点开始。(386,473) (177,454) (154,383) (363,402)

车牌号：CCPD中的每个图像只有一个车牌。每个车牌号码由一个汉字，一个字母和五个字母或数字组成。有效的中文车牌由七个字符组成：省（1个字符），字母（1个字符），字母+数字（5个字符）。
“ 0_0_22_27_27_33_16”是每个字符的索引。这三个数组定义如下。每个数组的最后一个字符是字母O，而不是数字0。我们将O用作“无字符”的符号，因为中文车牌字符中没有O。
'''
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
    return img.shape[0], img.shape[1],img.shape[2]

def main():
    xml_folder = r"C:\Users\Carpenter\Desktop\xml"
    img_folder = r"C:\Users\Carpenter\Desktop\CCPD2020\ccpd_green\total"
    for file in os.listdir(img_folder):
        if (file.endswith(".jpg") or file.endswith(".JPG")):
            strings = file.split("-")
            pos_str = strings[2]
            value_str = pos_str.split("_")
            xy1 = value_str[0].split("&")
            xy2 = value_str[1].split("&")
            x1 = xy1[0]
            y1 = xy1[1]
            x2 = xy2[0]
            y2 = xy2[1]

            print("str: ",pos_str)

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
