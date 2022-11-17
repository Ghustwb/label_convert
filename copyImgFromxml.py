#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据xml文件复制img文件
根据img文件复制xml文件
"""

import os
from tqdm import tqdm

xml_dir = r"C:\Users\Carpenter\Downloads\liuyifan-no_13\no_13\Annotations"
img_dir = r"C:\Users\Carpenter\Downloads\liuyifan-no_13\no_13\JPEGImages"


save_img_dir = img_dir + "_save"
if(not os.path.exists(save_img_dir)):
    print("Create Img folder to save")
    os.mkdir(save_img_dir)

save_xml_dir = xml_dir + "_save"
if(not os.path.exists(save_xml_dir)):
    print("Create XML folder to save")
    os.mkdir(save_xml_dir)

#list all video files
xmls_list = os.listdir(xml_dir)
xmls_list = tqdm(xmls_list)
for xml in xmls_list:
    xml_base_name= os.path.basename(xml)
    img_name = xml_base_name[:-4] + ".jpg"
    if os.path.exists(os.path.join(img_dir,img_name)):
        #copy img to save_dir
        img_path = os.path.join(img_dir,img_name)
        save_img_path = os.path.join(save_img_dir,img_name)
        print(f"copy {img_path} to {save_img_path}")
        os.system(f"copy {img_path} {save_img_path}")


#list all video files
imgs_list = os.listdir(img_dir)
imgs_list = tqdm(imgs_list)
for img in imgs_list:
    img_base_name= os.path.basename(img)
    xml_name = img_base_name[:-4] + ".xml"
    if os.path.exists(os.path.join(xml_dir,xml_name)):
        #copy img to save_dir
        xml_path = os.path.join(xml_dir,xml_name)
        save_xml_path = os.path.join(save_xml_dir,xml_name)
        #print(f"copy {xml_path} to {save_xml_path}")
        os.system(f"copy {xml_path} {save_xml_path}")
    