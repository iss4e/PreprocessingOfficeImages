import os
from PIL import Image, ImageDraw, ImageOps
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile
import random
from collections import defaultdict

"""
    Provides stats about labelled split images (those with &<num>.jpg filenames only!)
    Prints out the number of images per index, and per classification (occupied or not)
    
    usage: python stats_split_image.py <path to split labelled images)
"""
image_folder_path = sys.argv[1]

listOfFiles = os.listdir(image_folder_path)
lenFiles = len(listOfFiles)

index_to_images = defaultdict(list)
spatial_positions = ["top left    ", "top right   ", "bottom left ", "bottom right", "center      "]
class_name = ["0 Not Occ","1 Occ    "]

for i, filename in enumerate(listOfFiles):
    name, ext = filename.split('.')
    
    if ext == 'txt':
        _, image_number = name.split('&')
        
        with open(os.path.join(image_folder_path, filename), 'r') as f:
            
            class_val = f.read()
            if class_val == "0":
                index_to_images[(image_number,0)].append(name)
            elif class_val == "1":
                index_to_images[(image_number,1)].append(name)
       
prnt_seq = []       
for k,v in index_to_images.iteritems():
    prnt_seq .append( " {} | Index {}:{} number of imgs: {}".format(class_name[k[1]], k[0], spatial_positions[int(k[0])], len(v)))
    
prnt_seq.sort()
for i, item in enumerate(prnt_seq):
    print item
    if i == 4:
        print "----------------------------------------------------------------------"