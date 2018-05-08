import os
from PIL import Image
import sys
import ntpath
from tqdm import tqdm

"""
Crops the raw images to the desired dimensions, and prepends the date (directory name) to the images

To use: python crop_images.py <raw image raw_image_path> <output raw_image_path>
"""
raw_image_path = sys.argv[1]
output_path = sys.argv[2]

listOfFiles = os.listdir(raw_image_path)
dir_name = ntpath.basename(raw_image_path)


for filename in tqdm(listOfFiles):
    file = os.raw_image_path.join(raw_image_path, filename)
    img = Image.open(file) 
    img2  = img.rotate(-4.5)
    img2 = img2.crop((736,592,2354 + 736,1243 + 592))
    
    new_name = "{}_{}".format(dir_name.lower(), filename)
    new_path = ntpath.join(output_path, new_name)
    
    img2.save(new_path)


