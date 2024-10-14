# -*- coding: utf-8 -*-
import cv2


#파일 경로
FilePath = './video.mp4'

#Open the File
movie = cv2.VideoCapture(FilePath) #동영상 핸들 얻기

#Check that the file is opened
if movie.isOpened() == False: #동영상 핸들 확인
    print('Can\'t open the File' + (FilePath))
    exit()

#create the window & change the window size
#윈도우 생성 및 사이즈 변경
cv2.namedWindow('Face')

face_cascade = cv2.CascadeClassifier()
face_cascade.load('./haarcascade_frontalface_default.xml')


while(True):
    #read from movie file
    #동영상에서 이미지 얻기
    ret, frame = movie.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #grayframe = cv2.equalizeHist(grayframe)

    faces = face_cascade.detectMultiScale(grayframe, 1.1, 3, 0, (10, 10))
    """
    cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[,
                                           flags[, minSize[, maxSize]]]]]) → objects
    image 실제 이미지
    objects [반환값] 얼굴 검출 위치와 영역 변수
    scaleFactor 이미지 스케일
    minNeighbors 얼굴 검출 후보들의 갯수
    flags 이전 cascade와 동일하다 cvHaarDetectObjects 함수 에서
          새로운 cascade에서는 사용하지 않는다.
    minSize 가능한 최소 객체 사이즈
    maxSize 가능한 최대 객체 사이즈
    """
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
    """
    cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None
    img 적용할 이미지
    pt1 그릴 상자의 꼭지점
    pt2 pt1의 반대편 꼭지점
    color 상자의 색상
    thickness 상자의 라인들의 두께 음수 또는 CV_FILLED를 주면 상자를 채운다.
    lineType 라인의 모양 line()함수 확인하기
    shift ?? Number of fractional bits in the point coordinates.
    포인트 좌표의 분수 비트의 수??
    """

    cv2.imshow('Face',frame)

    #wait keyboard input until 1ms
    if cv2.waitKey(255) < 0:
    # if cv2.waitKey(1) != 255:
        break

#close the window
#윈도우 종료

# 10초 동안 키입력 기다립니다.
k = cv2.waitKey(10000)
movie.release()
# s키를 누르면 f1.jpg로 이미지 저장 후 종료
# 다른키 입력시 종료
# 키입력 없을시 10초간 대기
if k == ord('s'):
    cv2.imwrite('f1.jpg', frame)

cv2.destroyWindow('Face')
