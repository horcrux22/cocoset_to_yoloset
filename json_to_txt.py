import json
import os
import consts
import shutil
from PIL import Image


def find_filename(directory_name):
    file_lists = os.listdir(directory_name)
    file_lists = list(filter(lambda x: x[7:] == '.json', file_lists))
    file_lists = list(map(lambda x: x[:7], file_lists))

    return file_lists


def convert(directory_name, file_list, child):

    for file_name in file_list:
        path = directory_name + "/" + file_name + ".json"
        img_path = directory_name + "/" + file_name + ".jpg"
        f = open(consts.LABELS + '/' + child + '_' + file_name + ".txt", 'w')

        with open(path, 'rt', encoding='utf-8-sig') as json_file:
            json_data = json.load(json_file)

        with Image.open(img_path) as img:
            width, height = img.size

        dict_data = json_data[0][consts.JSON_INDEX]
        YOLO_CLASS_NUMBER = 0
        for i in dict_data:
            x = float(dict_data[i][0])
            y = float(dict_data[i][1])
            w = float(dict_data[i][2])
            h = float(dict_data[i][3])
            X = ((x + (w / 2)) / width)
            Y = ((y + (h / 2)) / height)
            W = (w / (width))
            H = (h / (height))
            print(YOLO_CLASS_NUMBER, X, Y, W, H, file=f)
            YOLO_CLASS_NUMBER += 1

        f.close()


def move_jpg(directory_name, file_list, child):
    for file_name in file_list:
        shutil.move(directory_name + '/' + file_name + '.jpg',
                    consts.IMAGES + '/' + child + '_' + file_name + '.jpg')
