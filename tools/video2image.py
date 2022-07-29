#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将video转image
"""

import os
import cv2

video_dir = r"C:\Users\Carpenter\Desktop\car_record\z50"
save_image_dir = r"C:\Users\Carpenter\Desktop\save_image"
factor = 100
crop_factor = 0.8

#list all video files
video_list = os.listdir(video_dir)
for video in video_list:
    video_name = os.path.join(video_dir, video)
    video_capture = cv2.VideoCapture(video_name)
    if not video_capture.isOpened():
        print("open video failed: ", video_name)
        continue
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    print(f"{video_name} has {frame_count} frames, {frame_width}x{frame_height}, {fps} fps")
    for i in range(frame_count):
        ret, frame = video_capture.read()
        if ret and (i % factor == 0):
            #crop the image based on factor
            start_pix = int(frame_width*(1 - crop_factor)/2)
            framet = frame[0:int(frame_height*crop_factor), start_pix:start_pix + int(frame_width*crop_factor)]
            cv2.imshow("framet", framet)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)

            image_name = os.path.join(save_image_dir, video[:-4] + "_" + str(i) + ".jpg")
            cv2.imwrite(image_name, framet)
            print(f"{i}/{frame_count}")
        i = i + 1
     