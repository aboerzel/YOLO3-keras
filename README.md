# YOLO3 (Detection, Training, and Evaluation)

https://github.com/experiencor/keras-yolo3
https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088
https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/

## Detection

## Training

### 1. Data preparation 
[Create Dataset](create-dataset.ipynb)

### 2. Edit the configuration file

### 3. Generate anchors for your dataset (optional)

### 4. Start the training process

`python train.py -c config.json`

### 5. Perform detection using trained weights on image, set of images, video, or webcam

`python predict.py -c config.json -i /path/to/image/or/video`

It carries out detection on the image and write the image with detected bounding boxes to the same folder.

