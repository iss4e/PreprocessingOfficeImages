import os
from PIL import Image, ImageDraw
import sys
import ntpath
from tqdm import tqdm

processed_path = sys.argv[1]

listOfFiles = os.listdir(processed_path)

lenFiles = len(listOfFiles)/2

center_factor = 104
    
for i, filename in enumerate(listOfFiles):
    name, exten = os.path.splitext(filename)
    
    if  'txt' in exten:
        continue
    
    file = os.path.join(processed_path, filename)
    img = Image.open(file) 
    width, height = img.size
    
    draw =ImageDraw.Draw(img)

    draw.rectangle(((width/4 - center_factor, height/4), (3*width/4 - center_factor, 3*height/4)), outline='red')
    img.show()
    
    text_path = os.path.join(processed_path, name + '.txt')
    
    input_string = raw_input("Enter string for file # {}/{} : ".format(i/2, lenFiles))
    
    with open(text_path,'r+') as txt_file:
        data = txt_file.read()
        new_data = data[:-1] + input_string
        txt_file.seek(0)
        txt_file.write(new_data)
        txt_file.truncate()
    

    
    


