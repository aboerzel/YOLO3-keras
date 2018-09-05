import xml.etree.ElementTree as ET
from imutils import paths
import argparse


def extract_annotations_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename').text
    # set image filepath relative to the dataset folder
    root.find('path').text = "/images/" + filename
    tree = ET.ElementTree(root)
    tree.write(xml_file)


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="dataset folder")
args = vars(ap.parse_args())

# the annotation folder contains the voc annotation files
image_paths = list(paths.list_files(args["dataset"] + "/" + "annotations", ".xml"))

for image_path in image_paths:
    extract_annotations_from_xml(image_path)
