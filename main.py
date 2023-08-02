import os
import shutil
 
from pytube import YouTube

def url_to_mp3(video_url:str):
    video_file = YouTube(video_url).streams.filter().get_audio_only()
    video_file.download()

    mp4_name:str = video_file.default_filename
    mp3_name:str = mp4_name.replace('.mp4','.mp3')## here we replaced the .mp4 file with .mp3 file extension
    os.rename(mp4_name, mp3_name)

    ##used to move the file
    shutil.move(mp3_name, 'audio')

def main():
    try:
        input_url:str = input('Please enter a URL::')
        url_to_mp3(video_url=input_url)
        print('Finished downloading')
    except Exception as e:
        print(f'Something went wrong::{e}')

if __name__=='__main__':
    main()