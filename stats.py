import os
from PIL import Image, ImageDraw
from collections import defaultdict
import sys
import random

processed_path = sys.argv[1]

listOfFiles = os.listdir(processed_path)
lenFiles = len(listOfFiles)

category_to_image = defaultdict(list)

for i, filename in enumerate(listOfFiles):
    name, ext = filename.split('.')
    
    if ext == 'txt':
        with open(os.path.join(processed_path, filename), 'r') as f:
            category = f.read()
            category_to_image[category].append("{}.jpg".format(name))
            

right_bottom_images = category_to_image["00010"]
random.shuffle(right_bottom_images)
category_to_image["00010"] = right_bottom_images[:150]

num_per_index = defaultdict(list)
for category, image_list in category_to_image.iteritems():
    print "{}  has {} elements".format(category, len(image_list))
    
    for i in range(5):
        if category[i] == '1':
            num_per_index[i].extend(image_list)      
sum_i  =0   
print "-------------------------------------------------------"
for index, number_of_imgs in num_per_index.iteritems():
    print "Index {} has {}/{} images".format(index, len(number_of_imgs), lenFiles/2)
    sum_i += len(number_of_imgs)
print "sum ", sum_i

num_per_index = defaultdict(list)
for category, image_list in category_to_image.iteritems():
    
    for i in range(5):
        if category[i] == '0':
            num_per_index[i].extend(image_list)
            
print "-------------------------------------------------------"
sum_i = 0
for index, number_of_imgs in num_per_index.iteritems():
    print "Index {} has {}/{} images".format(index, len(number_of_imgs), lenFiles/2)
    sum_i += len(number_of_imgs)
print "sum ", sum_i
    
# for filename in num_per_index[1]:
    # file = os.path.join(processed_path, filename)
    # print os.path.isfile(file)
    
    # img = Image.open(file) 
    # img.show()
    # input = raw_input("opening file: {} ".format(filename))
    
    # img.close()
            
    
