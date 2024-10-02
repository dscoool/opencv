// 카메라 출력 - 로컬에서 실행하여야 합니다
// .py 파일로 로컬에 저장 후 실행하세요. 
//카메라 연동은 colab이나 ipynb에서 지원하지 않습니다.
  
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
