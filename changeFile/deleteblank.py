#!/usr/bin/python
#-*- encoding: utf-8 -*-

# 비어있는 텍스트파일 지우기

import os, sys

path = '/home/foscar/바탕화면/yolov7_custom/yolov7-custom/data/train/labels/'
file_list = os.listdir(path)

print('FILE CNT : {}'.format(len(file_list)))
file_cnt = 0
for file in file_list:
    cnt_falg = 0
    f_read = open(path+file, 'r').read()
    out_str = ''
    for line in f_read.strip('\n').split('\n'):
        words = line.split()
        if int(words[0]) == 11:
            cnt_falg=1
            # print(path+file)
    if cnt_falg == 1:
        file_cnt +=1
print("COUNT::::", file_cnt)
        # if len(line) == 0: 
        #     print(path+file)
        #     os.remove(path+file) 