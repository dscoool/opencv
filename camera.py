# 카메라 출력 - 로컬에서 실행하여야 합니다
# 반드시 .py 파일로 '로컬'에 저장 후 실행하세요. 
# ipynb 지원불가
  
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    # 키입력이 있으면 탈출
    if cv2.waitKey(33) != -1:
        break  # Exit the loop if any key is pressed


capture.release()
cv2.destroyAllWindows()

# exe파일로 만들어서 배포하기 [pyinstaller]
# (PyInstaller 대소문자 구별)
# $ python -m pip install pyinstaller
# $ python -m PyInstaller --onefile --windowed camera.py
# .exe 파일은 dist 폴더 안에 생성됩니다.