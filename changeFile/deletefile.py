#!/usr/bin/python
#-*- encoding: utf-8 -*-

# 비어있는 텍스트파일 지우기

import os, sys

path = '/home/foscar/바탕화면/yolov7_custom/yolov7-custom/data/train/labels/'
file_list = os.listdir(path)

file_cnt = 0
cnt_falg = 0
for file in file_list:
    # print(file[0:5])
    if file[0:5] == "jhcar":
        print(file)
        os.remove(path+file) 

print('FILE CNT : {}'.format(len(file_list)))