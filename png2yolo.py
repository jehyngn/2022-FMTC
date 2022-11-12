'''
Created on Aug 18, 2021

@author: xiaosonh
'''
import os
import sys
import argparse
import shutil
import math
from collections import OrderedDict

import json
import cv2
import PIL.Image



class Labelme2YOLO(object):
    
    def __init__(self, json_dir):
        self._json_dir = json_dir
        
        self._label_id_map = self._get_label_id_map(self._json_dir)
        
                
    def _get_label_id_map(self, json_dir):
        label_set = set()
    
        for file_name in os.listdir(json_dir):
            if file_name.endswith('json'):
                json_path = os.path.join(json_dir, file_name)
                data = json.load(open(json_path))
                # for shape in data['shapes']:
                #     label_set.add(shape['label'])
        
        return OrderedDict([(label, label_id) \
                            for label_id, label in enumerate(label_set)])
                
    def convert_one(self, json_name):
        # json_path = os.path.join(self._json_dir, json_name)
        # json_data = json.load(open(json_path))
        
        json_names = [file_name for file_name in os.listdir(self._json_dir) \
                    if os.path.isfile(os.path.join(self._json_dir, file_name)) and \
                    file_name.endswith('.png')]


        print('Converting %s ...' % json_name)

        #print(json_path)
        ####### 여기 수정 ########
        # json_names 에 .png list로 들어감
        # png 폴더를 받고
        # 폴더에서 .png을 하나씩 뽑으면서 
        # for path in json_path

        for path in json_names:

            json_path = os.path.join(self._json_dir, path) # path : .png 경로
            # json_data = json.load(open(json_path)) # json 내 데이터 가져오는건데 필요 없는듯

            # json 파일이랑 같은 이름의 Png 파일 path 가져오는 함수 -> png 경로로 이미 받아와서 필요 없음
            # img_path = self._save_yolo_image(json_data, path, 
            #                                 self._json_dir, '')
            
            # yolo_obj_list = self._get_yolo_object_list(json_data, img_path)
            yolo_obj_list = self._get_yolo_object_list2(json_path)

            self._save_yolo_label(path, self._json_dir, 
                                '', yolo_obj_list)
    
    def _get_yolo_object_list2(self, img_path):
        yolo_obj_list = []
        img_h, img_w, _ = cv2.imread(img_path).shape
        yolo_obj = self._get_shape_yolo_object2(img_h, img_w)
        yolo_obj_list.append(yolo_obj)

        return yolo_obj_list



    def _get_shape_yolo_object2(self, img_h, img_w):

        label_id = 0 # 0 : None, 1 : Emergency

        obj_center_x = img_w / 2.0 # 
        obj_center_y = img_h / 2.0 # 
        obj_w = img_w
        obj_h = img_h

        dw = 1.0 / img_w
        dh = 1.0 / img_h
        
        yolo_center_x= round(float(obj_center_x *dw), 6)
        yolo_center_y = round(float(obj_center_y *dh), 6)
        yolo_w = round(float(obj_w * dw), 6)
        yolo_h = round(float(obj_h * dh), 6)

        return label_id, yolo_center_x, yolo_center_y, yolo_w, yolo_h

    
    def _save_yolo_label(self, json_name, label_dir_path, target_dir, yolo_obj_list):
        txt_path = os.path.join(label_dir_path, 
                                target_dir, 
                                json_name.replace('.png', '.txt'))

        with open(txt_path, 'w+') as f:
            for yolo_obj_idx, yolo_obj in enumerate(yolo_obj_list):
                yolo_obj_line = '%s %s %s %s %s\n' % yolo_obj \
                    if yolo_obj_idx + 1 != len(yolo_obj_list) else \
                    '%s %s %s %s %s' % yolo_obj
                f.write(yolo_obj_line)
                
    # def _save_yolo_image(self, json_data, json_name, image_dir_path, target_dir):
    #     img_name = json_name.replace('.json', '.png')
    #     print(img_name)
    #     img_path = os.path.join(image_dir_path, target_dir,img_name)
    #     print(img_path)
    #     # if not os.path.exists(img_path):
    #     #     img = utils.img_b64_to_arr(json_data['imageData'])
    #     #     PIL.Image.fromarray(img).save(img_path)
        
    #     return img_path
    
    def _save_dataset_yaml(self):
        yaml_path = os.path.join(self._json_dir, 'YOLODataset/', 'dataset.yaml')
        
        with open(yaml_path, 'w+') as yaml_file:
            yaml_file.write('train: %s\n' % \
                            os.path.join(self._image_dir_path, 'train/'))
            yaml_file.write('val: %s\n\n' % \
                            os.path.join(self._image_dir_path, 'val/'))
            yaml_file.write('nc: %i\n\n' % len(self._label_id_map))
            
            names_str = ''
            for label, _ in self._label_id_map.items():
                names_str += "'%s', " % label
            names_str = names_str.rstrip(', ')
            yaml_file.write('names: [%s]' % names_str)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_dir',type=str,
                        help='Please input the path of the labelme json files.')
    parser.add_argument('--val_size',type=float, nargs='?', default=None,
                        help='Please input the validation dataset size, for example 0.1 ')
    parser.add_argument('--json_name',type=str, nargs='?', default=None,
                        help='If you put json name, it would convert only one json file to YOLO.')
    args = parser.parse_args(sys.argv[1:])
         
    convertor = Labelme2YOLO(args.json_dir)
    if args.json_name is None:
        convertor.convert(val_size=args.val_size)
    else:
        convertor.convert_one(args.json_name)
    
