
import argparse
from imutils import paths
from utils import AspectAwarePreprocessor
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="images folder")
args = vars(ap.parse_args())

# the annotation folder contains the voc annotation files
image_paths = list(paths.list_files(args["dataset"] + "/" + "images", ".jpg"))

ap = AspectAwarePreprocessor(640)

for image_path in image_paths:
    img = cv2.imread(image_path)
    img = ap.preprocess(img)
    target_name = "output/" + image_path.split("\\")[-1]
    cv2.imwrite(target_name.lower(), img)
