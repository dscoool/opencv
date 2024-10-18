# Required libraries
import tkinter as tk
from tkinter import simpledialog, messagebox
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Function for downloading the video
def youtube_downloader(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)  # YouTube object
        print(f"Title: {yt.title}")  # Print the video title
        ys = yt.streams.get_highest_resolution()  # Set the highest resolution stream
        ys.download()  # Download the video
        messagebox.showinfo("Download Complete", f"Video '{yt.title}' has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI window for input
def get_url():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    url = simpledialog.askstring("YouTube Downloader", "Enter the YouTube URL:")
    
    if url:
        youtube_downloader(url)
    else:
        messagebox.showwarning("Input Required", "Please enter a valid URL!")

if __name__ == "__main__":
    get_url()

# exe파일로 만들어서 배포하기 [pyinstaller]
# C:\Users\sys\Desktop\openCV\youtube_downloader_win.py
# $ python -m pip install pyinstaller
# $ python -m PyInstaller --onefile 
#          --windowed youtube_downloader_win.py
## (PyInstaller 대소문자 구별)
# .exe 파일은 dist 폴더 안에 생성됩니다.
