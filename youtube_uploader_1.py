# !pip install pytubefix
# c:> python -m pip install pytubefix
from pytubefix import YouTube
from pytubefix.cli import on_progress

# v="VSQshAgnals" --> video ID 유일성
def youtube_downloader(url):
    # yt = 유튜브 객체(Object) 선언
    yt = YouTube(url,
            on_progress_callback=on_progress)

    print(yt.title) # 제목 출력
    #가능한 최대 해상도 설정
    ys = yt.streams.get_highest_resolution()
    ys.download() #유튜브를 파일로 다운로드

if __name__ == "__main__":
    url = input('Enter the Youtube url: ')
    # url = "https://www.youtube.com/watch?v=VSQshAgnals"
    youtube_downloader(url)
