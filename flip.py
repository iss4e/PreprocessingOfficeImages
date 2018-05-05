import os
from PIL import Image, ImageDraw, ImageOps
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile

processed_path = sys.argv[1]

listOfFiles = os.listdir(processed_path)
lenFiles = len(listOfFiles)

for filename in tqdm(listOfFiles):
    name, exten = os.path.splitext(filename)
    
    if  'txt' in exten:
        continue
    
    file = os.path.join(processed_path, filename)
    
    img = Image.open(file) 
    img = ImageOps.mirror(img)
    
    mirror_name = "{}_f".format(filename.split('.')[0])
    img.save(os.path.join(processed_path, mirror_name + '.jpg'))
    
    text_filename = mirror_name + '.txt'
    old_text_filename = filename.split('.')[0] + '.txt'
    
    new_text_path = os.path.join(processed_path, text_filename)
    old_text_path = os.path.join(processed_path, old_text_filename)
    
    copyfile(old_text_path, new_text_path)
    

    



