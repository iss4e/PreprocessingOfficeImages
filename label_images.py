import os
from PIL import Image, ImageDraw
import sys
import ntpath
from tqdm import tqdm

"""
Used for labelling photos that have already been cropped.
Displays an image to be labelled, divided into 4 quadrants, and center.

To label the image, type in the binary vector representing the occupancy of the image.
If 'd' is typed, the images are dumped into a folder for dark images, where the office is completely dark (not used in training)
if 'e' is typed, the images are dumped into a folder for images with all  5 regions empty. (this is for balancing the number of images with positive and negative examples)

This script should be run as follows 'python label_images.py <cropped photos path> <dark folder path> <empty folder path>

The vector should be a string of 5 binary values (such as "10000"), in the following order:
[top left, top right, bottom left, bottom right, center]

"""
cropped_photos_path = sys.argv[1]
dark_folder_path = sys.argv[2]
empty_folder_path = sys.argv[3]

listOfFiles = os.listdir(cropped_photos_path)
lenFiles = len(listOfFiles)

# the number of pixels the center quadrant is offset to the left of the true center of the image
center_offset = 104

for i, filename in enumerate(listOfFiles):
    name, ext = filename.split('.')
    
    if ext != 'jpg':
        continue
        
    file = os.path.join(cropped_photos_path, filename)
    img = Image.open(file) 
    width, height = img.size
    
    draw =ImageDraw.Draw(img)
    draw.line((width/2, 0, width/2, height), fill='green', width=3)
    draw.line((0, height/2, width, height/2), fill='green', width=3)
    draw.rectangle(((width/4 - center_offset, height/4), (3*width/4 - center_offset, 3*height/4)), outline='red')
    img.show()
    
    text_filename = "{}.txt".format(filename.split('.')[0])
    text_path = os.path.join(cropped_photos_path, text_filename)
    
    input_string = raw_input("Enter string for file # {}/{} : ".format(i, lenFiles))
    
    if 'e' in input_string:
        os.rename(file, os.path.join(empty_folder_path,filename))
        continue
        
    if 'd' in input_string:
        os.rename(file, os.path.join(dark_folder_path, filename))
        continue
    
    assert len(input_string) == 5 , "The vector entered does not have a length of 5"
    
    with open(text_path,'w+') as txt_file:
        txt_file.write(input_string)
    

    
    


