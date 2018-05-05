import os
from PIL import Image, ImageDraw, ImageOps
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile
import random
from collections import defaultdict
import glob

"""
This script may be used if it is desired to label the split images individually, ie. split them into 5 regions first,
then label each individually.

To use: python label_split_images.py <images folder path>
"""
image_folder_path = sys.argv[1]
 
images = [img for img in glob.glob(os.path.join(image_folder_path, "*.jpg"))]
strip_images = [img.split(".")[0] for img in images]

len_imgs = len(strip_images)

for i, img_name in enumerate(strip_images):
    file_path = img_name + '.jpg'
    img = Image.open(file_path) 
    img.show()
    
    input_string = raw_input("Enter string for file {} # {}/{} : ".format(os.path.basename(img_name), i, len_imgs))
    
    txt_path = img_name + '.txt'
    
    with open(txt_path,'w+') as txt_file:
        txt_file.write(input_string)
