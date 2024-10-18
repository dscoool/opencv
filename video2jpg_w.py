import cv2
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# 작업할 파일명을 지정해 줍니다.
# filepath = './video.mp4'

def get_filename():
    root = tk.Tk()  # 여기에서 괄호를 추가했습니다.
    root.withdraw()  # tkinter 창 숨기기
    
    filename = simpledialog.askstring("Video2Image Converter", "Enter the filename:")
    
    if filename:
        mp4tojpg(filename)
    else:
        messagebox.showwarning("Input Required", "Please enter a valid filename!")

def mp4tojpg(filepath):
    video = cv2.VideoCapture(filepath)  # 비디오 파일 로드
    
    if not video.isOpened():
        messagebox.showwarning("Could not Open :", filepath)
        exit(0)

    # 비디오 파일의 정보 출력
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print("length :", length)
    print("width :", width)
    print("height :", height)
    print("fps :", fps)

    # 프레임을 저장할 디렉토리를 파일명과 동일하게 생성
    try:
        if not os.path.exists(filepath[:-4]):
            os.makedirs(filepath[:-4])
    except OSError:
        messagebox.showwarning('Error: Creating directory. ' + filepath[:-4])

    count = 0

    while(video.isOpened()):
        ret, image = video.read()
        if not ret:  # 더 이상 프레임이 없으면 루프 종료
            break

        if int(video.get(1)) % fps == 0:  # FPS에 맞춰 1초마다 프레임 추출
            cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
            messagebox.showwarning('Saved frame number:', str(int(video.get(1))))
            count += 1

    video.release()
    messagebox.showwarning("Video processing complete.")

if __name__ == "__main__":
    get_filename()
