import os
from PIL import Image, ImageDraw, ImageOps
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile
import random
from collections import defaultdict

"""
Shrinks the dataset of positive and negative examples,
 based on the numbers specified in the 'images_per_spatial_location' array.
 
 This array specifies how many  examples should be kept of each index
 ie. [top left, top right, bottom left, bottom right, center].
 
 After this program is run, the folder will contain the specified number of images per spatial location
 for both positive and negative examples at that index.
 
For example, if the first element in the array is 100, 
there will be 100 occupied and 100 unoccupied image for the top left quadrant after the program is run
 
 The array values should be chosen based on the output of 'stats_split_image.py'
 
 To use: python shrink_split_images.py <image folder path>
"""
image_folder_path = sys.argv[1]

listOfFiles = os.listdir(image_folder_path)
lenFiles = len(listOfFiles)

index_to_images = defaultdict(list)

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
            
images_per_spatial_location = [151, 167, 165, 180, 105]

for index, images in index_to_images.iteritems():
    random.shuffle(images)
    
    
    images = images[ images_per_spatial_location[int(index[0])] : ]
    
    for image in images:
        text_file = os.path.join(image_folder_path, image + '.txt')
        img_file = os.path.join(image_folder_path, image + '.jpg')
        
        os.remove(text_file)
        os.remove(img_file)
    

    



