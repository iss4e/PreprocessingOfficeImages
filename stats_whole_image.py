import os
from PIL import Image, ImageDraw
from collections import defaultdict
import sys
import random

"""
Provides stats about the labelled images for the user. Use *before* splitting the images.
To be exact, it displays how many images of each possible vector there are (00001, 00011...)
It also says how many positive and negative examples there are for each spatial region
example: top left images etc.

usage: python stats_whole_image.py <image folder path>

Note:
These stats are only including 150 of the "00010" type of image, due to the nature of the data.
Should be modified if data is different
"""

image_folder_path = sys.argv[1]

listOfFiles = os.listdir(image_folder_path)
lenFiles = len(listOfFiles)

category_to_image = defaultdict(list)

spatial_positions = ["top left    ", "top right   ", "bottom left ", "bottom right", "center      "]

for i, filename in enumerate(listOfFiles):
    name, ext = filename.split('.')
    
    if ext == 'txt':
        with open(os.path.join(image_folder_path, filename), 'r') as f:
            category = f.read()
            category_to_image[category].append("{}.jpg".format(name))
            

# HACK: in order to balance out the data used, I drop the images which contained a lot of 00010 examples
# Should be changed if the data is different
right_bottom_images = category_to_image["00010"]
random.shuffle(right_bottom_images)
category_to_image["00010"] = right_bottom_images[:150]

num_per_index = defaultdict(list)
for category, image_list in category_to_image.iteritems():
    print "{}  has {} images".format(category, len(image_list))
    
    for i in range(5):
        if category[i] == '1':
            num_per_index[i].extend(image_list)      
sum_i  =0   
print "-------------------------------------------------------"
print "Positive Examples - Occupied"
for index, number_of_imgs in num_per_index.iteritems():
    print "Index {}: {} {}/{} images".format(index, spatial_positions[index], len(number_of_imgs), lenFiles/2)
    sum_i += len(number_of_imgs)
print "sum ", sum_i

num_per_index = defaultdict(list)
for category, image_list in category_to_image.iteritems():
    
    for i in range(5):
        if category[i] == '0':
            num_per_index[i].extend(image_list)
            
print "-------------------------------------------------------"
print "Negative Examples - Unoccupied"
sum_i = 0
for index, number_of_imgs in num_per_index.iteritems():
    print "Index {}: {} {}/{} images".format(index, spatial_positions[index], len(number_of_imgs), lenFiles/2)
    sum_i += len(number_of_imgs)
print "sum ", sum_i
    
            
    
