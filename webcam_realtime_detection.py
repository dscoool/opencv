from ultralytics import YOLO
import cv2
import math

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set width
cap.set(4, 480)  # set height

# load YOLO model
model = YOLO("./yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    # run YOLO model on the frame
    results = model(img, stream=True)

    # draw bounding boxes and labels
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to integer values

            # draw the bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence score
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # class label
            cls = int(box.cls[0])
            class_name = classNames[cls]
            print("Class name -->", class_name)

            # put text on the image (labeling the object)
            org = (x1, y1 - 10)  # position for the label
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 0.6
            color = (255, 0, 0)  # blue color for the text
            thickness = 2
            cv2.putText(img, f'{class_name} {confidence}', org, font, fontScale, color, thickness)

    # display the image using OpenCV
    cv2.imshow('Webcam', img)

    # press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcam and close windows
cap.release()
cv2.destroyAllWindows()

# Ref: https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993

# exe파일로 만들어서 배포하기 [pyinstaller]
# (PyInstaller 대소문자 구별)
# $ python -m pip install pyinstaller
# $ python -m PyInstaller --onefile --windowed webcam_realtime_detection.py
# .exe 파일은 dist 폴더 안에 생성됩니다.
