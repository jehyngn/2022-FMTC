#!/usr/bin/python
#-*- encoding: utf-8 -*-

import os, sys

# 기존 데이터에서 신호등 클래스 빼고 다 지우기 (0~9)
# 10이상 클래스들은 다 삭제

# 기존 데이터 경로 
path = '/home/foscar/바탕화면/before/'
# 바꿔서 저장할 데이터 경로 
path2 = '/home/foscar/바탕화면/after/'
file_list = os.listdir(path)

print('FILE CNT : {}'.format(len(file_list)))
for file in file_list:
    f_read = open(path+file, 'r').read()

    out_str = ''
    for line in f_read.strip('\n').split('\n'):
        if len(line) == 0: continue
        words = line.split()
        if int(words[0]) >= 10:
            continue

        out_str += " ".join(words) + '\n'

    res_str = out_str.rstrip('\n')

    print(file)
    print(f_read.strip())
    print('=======================')
    print(res_str)
    print()

    with open(path2+file, 'w') as f:
        f.write(res_str)
        f.close()

