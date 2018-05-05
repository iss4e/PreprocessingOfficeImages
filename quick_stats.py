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
                index_to_images[(image_number,0)].append(name)
            elif class_val == "1":
                index_to_images[(image_number,1)].append(name)
       
prnt_seq = []       
for k,v in index_to_images.iteritems():
    prnt_seq .append( "Class # {} Img # {}, number of imgs: {}".format(k[1], k[0], len(v)))
    
prnt_seq.sort()
for item in prnt_seq:
    print item