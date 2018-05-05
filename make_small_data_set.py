import os
from PIL import Image, ImageDraw, ImageOps
import sys
import ntpath
from tqdm import tqdm
from shutil import copyfile
import random
from collections import defaultdict
import glob

processed_path = sys.argv[1]
 
images = [img for img in glob.glob(os.path.join(processed_path, "*.jpg"))]
strip_images = [img.split(".")[0] for img in images]

random.shuffle(strip_images)

for img in tqdm(strip_images[240 : ]):
    for exten in [".jpg", ".txt"]:
        file_path = img + exten
        os.remove(file_path)
    


    

    



