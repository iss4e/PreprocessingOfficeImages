import os
from PIL import Image
import sys
import ntpath
from tqdm import tqdm

path = sys.argv[1]
processed_path = sys.argv[2]

listOfFiles = os.listdir(path)
dir_name = ntpath.basename(path)


for filename in tqdm(listOfFiles):
    file = os.path.join(path, filename)
    img = Image.open(file) 
    img2  = img.rotate(-4.5)
    img2 = img2.crop((736,592,2354 + 736,1243 + 592))
    
    new_name = "{}_{}".format(dir_name.lower(), filename)
    new_path = ntpath.join(processed_path, new_name)
    
    img2.save(new_path)


