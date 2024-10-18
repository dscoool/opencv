import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# 이미지 인식 YOLO 모델을 로딩합니다. 버전 11.
# model = YOLO('yolov8n.pt')
model = YOLO('yolo11n-pose.pt')

# 이미지 로딩 (각자 파일 경로를 입력하세요)
image_path = './robbery.jfif'
# 이미지 출력 (결과파일 경로를 입력하세요)
output_path = './robbery_1.jfif'  # Ensure the output directory exists

image = cv2.imread(image_path)

# 물체 인식(객체인식, object detection)을 수행합니다.
results = model(image)

# BGR 이미지를 RGB 이미지로 변환
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 결과 출력
annotated_image = results[0].plot()  # Visualize the detection results on the image

# 결과 이미지를 output_path에 지정된 
# jpg파일로 저장합니다.
cv2.imwrite(output_path, annotated_image)

print(f'Annotated image saved to: {output_path}')

# 이미지 화면 출력을 위해 RGB로 변환합니다.
annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

# Matplotlib을 사용하여 이미지를 화면에 출력
plt.imshow(annotated_image_rgb)
plt.axis('off')  
plt.show()

