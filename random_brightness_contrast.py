import os
from PIL import Image, ImageEnhance
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile

import numpy

"""
    Adds random brightness and contrast to images in a path (in place)
    
    To use: python random_brightness_contrast.py <path to images>
    Note: Adjust the deviation values to change the strength of image enhancements (second arg in normal function)
"""
image_folder_path = sys.argv[1]

listOfFiles = os.listdir(image_folder_path)
lenFiles = len(listOfFiles)

for filename in tqdm(listOfFiles):
    name, exten = os.path.splitext(filename)
    
    if  'txt' in exten:
        continue
    
    file = os.path.join(image_folder_path, filename)
    
    img = Image.open(file) 
    
    transformed_images = [img for i in range(2)]
    
    
    for i, tr_image in enumerate(transformed_images):
    
        contrast_value = numpy.random.normal(1,0.08)
        brightness_value = numpy.random.normal(1,0.15)
        
        #contrast_value = 1 + 2 * 0.08
        #brightness_value = 1 + 2 * 0.15
        
        b_enhancer = ImageEnhance.Brightness(tr_image)
        
        tr_image = b_enhancer.enhance(brightness_value)
        
        c_enhancer  = ImageEnhance.Contrast(tr_image)
        tr_image = c_enhancer.enhance(contrast_value)
        
        transformed_name = "{}__{}".format(name, i)
        tr_image.save(os.path.join(image_folder_path, transformed_name +'.jpg'))
        
        text_filename = transformed_name + '.txt'
        old_text_filename = name + '.txt'
    
        new_text_path = os.path.join(image_folder_path, text_filename)
        old_text_path = os.path.join(image_folder_path, old_text_filename)
        
        copyfile(old_text_path, new_text_path)



