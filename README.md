# Under conctruction...

# Real-time object detection with YOLO 3 (Keras)

Pyhon-Framework zur Erkennung und Lokalisierung von Objekten in Bildern und Videostreams in Echtzeit. Das Framework basiert auf der [YOLO 3](notebook/YOLOv3.pdf) Implementierung (https://github.com/experiencor/keras-yolo3) von (https://github.com/experiencor).

## YOLO (You only look once)
Im Vergleich zu anderen Methoden wie [SSD](https://arxiv.org/abs/1512.02325), [DSSD](https://arxiv.org/abs/1701.06659), [R-FCN](https://arxiv.org/abs/1605.06409), [RetinaNet](https://arxiv.org/abs/1708.02002) , ect. arbeitet [YOLO 3](notebook/YOLOv3.pdf) exterm schnell bei hoher Präzision (siehe https://pjreddie.com/darknet/yolo), daher ist [YOLO 3](notebook/YOLOv3.pdf) extrem gut für die Objekterkennung in Echtzeit geeignet. Während für das Training eine entsprechend gute GPU mit ausreichend Speicher benötigt wird, kann die Objekterkennung sogar auf weniger performanten CPUs wie beispielsweise einem [Raspberry PI 3](https://de.wikipedia.org/wiki/Raspberry_Pi) ausgeführt werden.

Hier einige Artikel zur Arbeitsweise von YOLO:
- https://medium.com/jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088
- https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/

## Anwendungsbeispiele:

#### Erkennung von Fahrzeugen, Verkehrszeichen und Personen in Echtzeit

![Beispiel](https://youtu.be/MiJpW9fhUdw)

#### Erkennung von Waschbären in Echtzeit

![Beispiel](notebook/videos/cars_on_the_road.mp4)

#### Erkennung von "Fabian" (Nachbar's Katze) in Echtzeit

![Beispiel](notebook/videos/cars_on_the_road.mp4)

## Training

