import os
from PIL import Image, ImageDraw
from collections import defaultdict
import sys
from shutil import copyfile
from tqdm import tqdm
import random


def split_image(image_name):
    
    img_path = os.path.join(processed_path, image_name + '.jpg')
    img = Image.open(img_path)
    
    width, height = img.size
    
    top_left = img.crop((0,0, width/2, height/2))
    top_right = img.crop((width/2, 0, width, height/2))
    
    
    bottom_left = img.crop((0, height/2, width/2, height - 1)) # need to sub 1 because width or height is uneven
    bottom_right = img.crop((width/2, height/2, width, height - 1))
    
    center_factor = 104

    
    center = img.crop((width/4 - center_factor, height/4, 3*width/4 - center_factor, 3*height/4 - 1))
    
    split_images = [top_left, top_right, bottom_left, bottom_right, center] # order is important due to indexing
    
    return split_images
   
     

processed_path = sys.argv[1]
output_path = sys.argv[2]

listOfFiles = os.listdir(processed_path)
lenFiles = len(listOfFiles)

category_to_image = defaultdict(list)

for i, filename in enumerate(listOfFiles):
    name, ext = filename.split('.')
    
    if ext == 'txt':
        with open(os.path.join(processed_path, filename), 'r') as f:
            category = f.read()
            category_to_image[category].append(name)
            
right_bottom_images = category_to_image["00010"]
random.shuffle(right_bottom_images)
category_to_image["00010"] = right_bottom_images[:150]
   
for category, image_list in category_to_image.iteritems():
    #print "{}  has {} elements".format(category, len(image_list))
    assert len(category) == 5
    
    for image in tqdm(image_list):
        split_images = split_image(image)
        
        for i, binary_value  in enumerate(category):
        
            split_name = "{}&{}".format(image, i)
             
            split_images[i].save(os.path.join(output_path, split_name + '.jpg'))
            
            txt_path = os.path.join(output_path, split_name + '.txt')
            
            with open(txt_path, 'w+') as txt_file:
                txt_file.write(binary_value)
            
            
    
        
       
       

 
 



    
    
