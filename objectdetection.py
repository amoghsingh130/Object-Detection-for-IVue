import torch
import cv2
import numpy as np
 
names = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 
        'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 
        'teddy bear', 'hair drier', 'toothbrush']
 
class personTrack:
    def __init__(self, maxPerson=1, modelClasses=0):
        self.maxPerson = maxPerson
        self.modelClasses = modelClasses
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.model.classes = modelClasses
 
    def findPerson(self, img):
        results = self.model(img)
        if len(results.xyxy[0].tolist()) >= 1:
            obj = results.xyxy[0].tolist()[0]
 
            x2 = int(obj[0])
            y2 = int(obj[1])
            x1 = int(obj[2])
            y1 = int(obj[3])
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            x1h = x1 
            y1h = int((y1 + y2) / 2)
            cxh = int((x2 + x1h) / 2)
            cyh = int((y2 + y1h) / 2)
 
            head = [x1h, y1h, x2, y2, cxh, cyh]
 
            return x1, y1, x2, y2, cx, cy, head
        else:
            return None, None, None, None, None, None, None
        
        def moveServo(cx, cy, x1, y1, x2, y2, frameheight, framewidth, centerframex1, centerframex2, centerframey1, centerframey2):
            if cx > centerframex2:
                #move servo negative
            elif cx < centerframex1:
                #move servo positive
            elif cy < centerframey1:
                #move servo negative
            elif cy > centerframey2:
                #move servo positive
        
 
pt = personTrack()
 
cap = cv2.VideoCapture(0) 
 
while True: 
    # Capture the video frame by frame 
    ret, frame = cap.read() 
    if ret:
        # Detect person and get bounding box coordinates
        x1, y1, x2, y2, cx, cy, _ = pt.findPerson(frame)
        
 
        # Draw bounding box if person is detected
        if x1 is not None:
            frame=cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
 
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
 
        # Check if 'q' key is pressed to quit
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
 
# Release the capture 
cap.release() 
 
# Destroy all the windows 
cv2.destroyAllWindows()

