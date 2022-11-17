# -*- coding: utf8 -*-
# PascalVoc格式转为YOLO格式
#
#!/usr/bin/env python
import os

f = open(r"C:\Users\Carpenter\Desktop\delete.txt")               # 返回一个文件对象  
line = f.readline()            
while line:  
    #print (line)    
    line = f.readline()   
    img = "D:\\TrainingData\\VOCdevkit\\VOC2007\\JPEGImages\\" + line[0:-1] + ".jpg"
    xml = "D:\\TrainingData\\VOCdevkit\\VOC2007\\Annotations\\" + line[0:-1] + ".xml"
    os.remove(img)
    os.remove(xml)
f.close()