# written by John Sha
# Referenced:
# https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
# https://stackoverflow.com/questions/9868963/cvimwrite-could-not-find-a-writer-for-the-specified-extension

import cv2
from imutils import paths
import argparse
import os

# parsing the arguments in command line for dataset parameter
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
args = vars(ap.parse_args())

# setting the path to the dataset for iterating through the image directory
imagePaths = list(paths.list_images(args["dataset"]))

path = args["dataset"] + "_resized"

# creating a folder for the images
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

# loop for resizing all images in directory
for (i, imagePath) in enumerate(imagePaths):
    image = cv2.imread(imagePath)

    print('Original Dimensions : ',image.shape)

    scale_percent = 15 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    print('Resized Dimensions : ',resized.shape)

    os.chdir(path)  # navigate inside new directory
    cv2.imwrite(str(i) + ".png", resized)
    os.chdir("..") # navigate out of directory

    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
