
import argparse
from imutils import paths
from utils import AspectAwarePreprocessor
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="images folder")
ap.add_argument("-o", "--output", default="output", required=True,
                help="output folder")
args = vars(ap.parse_args())

# the annotation folder contains the voc annotation files
image_paths = list(paths.list_images(args["dataset"]))

if not os.path.exists(args["output"]):
    os.makedirs(args["output"])

ap = AspectAwarePreprocessor(640)

for image_path in image_paths:
    img = cv2.imread(image_path)
    img = ap.preprocess(img)
    target_name = args["output"] + "/" + image_path.split("\\")[-1]
    cv2.imwrite(target_name.lower(), img)
