import os
from PIL import Image, ImageDraw, ImageOps
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile
import random
from collections import defaultdict

processed_path = sys.argv[1]

listOfFiles = os.listdir(processed_path)
lenFiles = len(listOfFiles)

index_to_images = defaultdict(list)

for i, filename in enumerate(listOfFiles):
    name, ext = filename.split('.')
    
    if ext == 'txt':
        _, image_number = name.split('&')
        
        with open(os.path.join(processed_path, filename), 'r') as f:
            
            class_val = f.read()
            if class_val == "0":
                index_to_images[image_number].append(name)
            
positive_class_num = [156, 167, 173, 263, 110]

for index, images in index_to_images.iteritems():
    random.shuffle(images)
    #print positive_class_num[int(index)]
    images = images[ positive_class_num[int(index)] : ]
    
    for image in images:
        text_file = os.path.join(processed_path, image + '.txt')
        img_file = os.path.join(processed_path, image + '.jpg')
        
        os.remove(text_file)
        os.remove(img_file)
    

    



