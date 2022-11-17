#检查label VOC
#
#
#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import cv2
import multiprocessing

sys.path.append("C:/Users/Carpenter/Documents/Code/label_convert")
sys.path.append("C:/Users/Carpenter/Documents/Code/label_convert/libs")
dir_name = os.path.abspath(os.path.dirname(__file__))
libs_path = os.path.join(dir_name, '..', 'libs')
sys.path.insert(0, libs_path)
sys.path.insert(0, dir_name)

from pascal_voc_io import PascalVocReader

xml_folder = "D:/TrainingData/VOCdevkit/VOC2007/no_empty/xml"

def checks(xml):
    in_file = open(os.path.join(xml_folder,xml), 'r', encoding='utf-8')
    infos = PascalVocReader(os.path.join(xml_folder, in_file))

    print(xml[:-4])
    print("***")
          

if __name__ == '__main__':
    xml_files = [name for name in os.listdir(xml_folder) if name.endswith('.xml')]
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            pool.map(checks, xml_files)
    pool.join()
