import os
from PIL import Image, ImageDraw
import sys
import ntpath
from tqdm import tqdm

processed_path = sys.argv[1]
move_path = sys.argv[2]
skip_path = sys.argv[3]

listOfFiles = os.listdir(processed_path)
lenFiles = len(listOfFiles)

for i, filename in enumerate(listOfFiles):
    file = os.path.join(processed_path, filename)
    img = Image.open(file) 
    width, height = img.size
    
    draw =ImageDraw.Draw(img)
    draw.line((width/2, 0, width/2, height), fill='green', width=3)
    draw.line((0, height/2, width, height/2), fill='green', width=3)
    img.show()
    
    text_filename = "{}.txt".format(filename.split('.')[0])
    text_path = os.path.join(processed_path, text_filename)
    
    input_string = raw_input("Enter string for file # {}/{} : ".format(i, lenFiles))
    
    if 's' in input_string:
        os.rename(file, os.path.join(skip_path,filename))
        continue
        
    if 'm' in input_string:
        os.rename(file, os.path.join(move_path, filename))
        continue
    
    with open(text_path,'w+') as txt_file:
        txt_file.write(input_string)
    

    
    


