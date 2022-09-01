#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据xml文件复制img文件
"""

import os

xml_dir = r"G:\CarRecordVideo\Annotation\z50_xml"
img_dir = r"G:\CarRecordVideo\Annotation\z50"


save_dir = img_dir + "_save"
if(not os.path.exists(save_dir)):
    print("Create folder to save")
    os.mkdir(save_dir)

#list all video files
xmls_list = os.listdir(xml_dir)
for xml in xmls_list:
    xml_base_name= os.path.basename(xml)
    img_name = xml_base_name[:-4] + ".jpg"
    if os.path.exists(os.path.join(img_dir,img_name)):
        #copy img to save_dir
        img_path = os.path.join(img_dir,img_name)
        save_img_path = os.path.join(save_dir,img_name)
        print(f"copy {img_path} to {save_img_path}")
        os.system(f"copy {img_path} {save_img_path}")
    