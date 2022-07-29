#检查label VOC
#
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

check_label = "LicensePlate"

def main():
    xml_folder = r"C:\Users\Carpenter\Desktop\tmp\xml"
    print(xml_folder)
    for file in os.listdir(xml_folder):
        if (file.endswith(".xml")):
            infos = PascalVocReader(os.path.join(xml_folder, file))
            for info in infos.shapes:
                if(info[0] != check_label):
                    print(file,"OK")
            

if __name__ == '__main__':
    main()
