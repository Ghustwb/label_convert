# -*- coding: utf8 -*-
# PascalVoc格式转为YOLO格式
#
#!/usr/bin/env python


import argparse
import multiprocessing
import os
import xml.etree.ElementTree
import shutil

from PIL import Image
from pascal_voc_writer import Writer


xml_dir = r'D:\TrainingData\VOCdevkit\VOC2007\Annotations'
image_dir = r'D:\TrainingData\VOCdevkit\VOC2007\JPEGImages'
yolo_dir = r'D:\TrainingData\yolo'
names = ['face','Licenseplate']

def yolo2voc(txt_file):
    w, h = Image.open(os.path.join(image_dir, txt_file[:-4] + ".jpg")).size
    writer = Writer(txt_file[:-4] + ".xml", w, h)
    with open(os.path.join(xml_dir, txt_file)) as f:
        for line in f.readlines():
            label, x_center, y_center, width, height = line.rstrip().split(' ')
            x_min = int(w * max(float(x_center) - float(width) / 2, 0))
            x_max = int(w * min(float(x_center) + float(width) / 2, 1))
            y_min = int(h * max(float(y_center) - float(height) / 2, 0))
            y_max = int(h * min(float(y_center) + float(height) / 2, 1))
            writer.addObject(names[int(label)], x_min, y_min, x_max, y_max)
    writer.save(os.path.join(xml_dir, txt_file[:-4] + ".xml"))


def voc2yolo(xml_file):
    in_file = open(os.path.join(xml_dir,xml_file), 'r', encoding='utf-8')
    try:
        root = xml.etree.ElementTree.parse(in_file).getroot()
    except Exception as e :
        print(xml_file[:-4])
        return
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    has_class = False
    for obj in root.iter('object'):
        name = obj.find('name').text
        if name in names:
            has_class = True
    if has_class:
        out_file = open(os.path.join(yolo_dir,xml_file[:-4] + ".txt"), 'w')
        for obj in root.iter('object'):
            name = obj.find('name').text
            if name in names:
                xml_box = obj.find('bndbox')
                x_min = float(xml_box.find('xmin').text)
                y_min = float(xml_box.find('ymin').text)
                x_max = float(xml_box.find('xmax').text)
                y_max = float(xml_box.find('ymax').text)

                box_x = (x_min + x_max) / 2.0 - 1
                box_y = (y_min + y_max) / 2.0 - 1
                box_w = x_max - x_min
                box_h = y_max - y_min
                box_x = box_x * 1. / w
                box_w = box_w * 1. / w
                box_y = box_y * 1. / h
                box_h = box_h * 1. / h

                b = [box_x, box_y, box_w, box_h]
                cls_id = names.index(obj.find('name').text)
                info = str(cls_id) + " " + " ".join([str(x) for x in b]) + '\n'
                #out_file.write(str(cls_id) + " " + " ".join([str(f'{a:.6f}') for a in b]) + '\n')
                out_file.write(info)
            else:
                print("no label",name )
    #print("saved: ",xml_file[:-4])
    else:
        print(xml_file[:-4])
        #shutil.move(os.path.join(xml_dir,xml_file),os.path.join(r"D:\tmp",xml_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--yolo2voc', action='store_true', help='YOLO to VOC')
    parser.add_argument('--voc2yolo', action='store_true', help='VOC to YOLO')
    args = parser.parse_args()

    if args.yolo2voc:
        print('YOLO to VOC')
        txt_files = [name for name in os.listdir(xml_dir) if name.endswith('.txt')]

        with multiprocessing.Pool(os.cpu_count()) as pool:
            pool.map(yolo2voc, txt_files)
        pool.close()

    if args.voc2yolo:
        print('VOC to YOLO')
        xml_files = [name for name in os.listdir(xml_dir) if name.endswith('.xml')]

        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            pool.map(voc2yolo, xml_files)
        pool.join()
        # for xml_file in xml_files:
        #     voc2yolo(xml_file)