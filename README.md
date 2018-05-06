## Preprocessing Office Images
The following scripts are used for processing gathered images of the lab office, in order to label them for CNN training purposes.
*Each script contains information on its precise usage in the file's documentation.*

The following order should be used for processing the office images:
1. `crop_image.py` - Crop the training images 
2. `label_images.py` - Label the images 
3. `stats_whole_image.py` - View statistics about the labelled images.
This provides information about how many occupied and unoccupied training 
(positive and negative, respectively) are in each spatial region of the office. 
This may encourage some adjustments, such as gathering additional training data.
4. `split_to_five.py` - Splits the labelled images into the five spatial regions of the office.
5. `stats_split_image.py` - Provides similar information to the whole image stats, namely, 
how many occupied and unoccupied images there are for each spatial image. It is important to note these numbers for the next step.
6. `shrink_split_images.py` - Using the noted numbers of occupied and unoccupied images, 
one can equalize the number of positive and negative training examples, by modifying the `images_per_spatial_location` array in the file.
As stated in the file, "if the first element in the array is 100, there will be 100 occupied and 100 unoccupied image
 for the top left quadrant after the program is run."  
 The rule of thumb is that the number at each spatial index should be `min(positive examples, negative examples)`.

You should now have a folder with an equal number of positive and negative labelled training examples at each spatial position.

___
Now, it is possible to perform some basic data augmentation in order to increase the size of the dataset:  
+ `flip_images.py` - Creates a labelled copy of each image with a horizontal flip applied (not necessary when using Caffe, as this can be specified during training)
+ `random_brightness_contrast.py` - Creates additional copies of each image, with random brightness and contrast applied to it. 
The strength of these image adjustments is controlled with random normal variables in the script.




