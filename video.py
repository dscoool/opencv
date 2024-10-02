// mp4 비디오 다루기
// mp4 비디오를 다운받은 후, 파일명을 수정하고
// 로컬에서 실행해 보세요!!

import cv2

// 이미지 파일명 수정
capture = cv2.VideoCapture("Image/Star.mp4") 

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
