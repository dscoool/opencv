# mp4 비디오 다루기
# mp4 비디오를 다운받은 후, 파일명을 수정하고
# 로컬에서 실행해 보세요!!

# 유튜브비디오 다운로더 - https://yt1d.com/

# pip install pytube opencv-python
import cv2
from pytube import YouTube

# 이미지 파일명 수정    

filename = input('Enter the mp4 filename: ')
capture = cv2.VideoCapture(filename) 

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
