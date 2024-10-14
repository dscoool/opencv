## 이 프로그램은 .mp4 파일 동영상을 분쇄하여
## .jpg 파일로 변환하는 예제입니다.
import cv2
import os

# cv2 버전 출력
print(cv2.__version__)

# 작업할 파일명을 지정해 줍니다.
filepath = './video.mp4'
video = cv2.VideoCapture(filepath) #'' 사이에 사용할 비디오 파일의 경로 및 이름을 넣어주도록 함

if not video.isOpened():
    print("Could not Open :", filepath)
    exit(0)

#불러온 비디오 파일의 정보 출력
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

print("length :", length)
print("width :", width)
print("height :", height)
print("fps :", fps)

#프레임을 저장할 디렉토리를 파일명과 동일하게 생성
# video.mp4 --> ./video/ 디렉토리 생성
try:
    if not os.path.exists(filepath[:-4]):
        os.makedirs(filepath[:-4])
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])


count = 0

while(video.isOpened()):
    ret, image = video.read()
    if not ret:  # Check if there are no more frames
        break  # Exit the loop when the video ends

    if(int(video.get(1)) % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1
        
video.release()
print("Video processing complete.")


# exe파일로 만들어서 배포하기 [pyinstaller]
# (PyInstaller 대소문자 구별)
# $ python -m pip install pyinstaller
# $ python -m PyInstaller --onefile --windowed video2image.py
# .exe 파일은 dist 폴더 안에 생성됩니다.