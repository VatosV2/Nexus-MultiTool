from Helper import *
from Helper.Common.utils import *

def download_youtube(url, file_type):
    try:
        yt = YouTube(url)
        if file_type == 'mp3':
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path="Output/Youtube")
            print(f"{lc} Audio downloaded successfully!")
        elif file_type == 'mp4':
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path="Output/Youtube")
            print(f"{lc} Video downloaded successfully!")
        else:
            print(f"{lc} Invalid file type. Please choose 'mp3' or 'mp4'.")
    except Exception as e:
        print(f"{lc} An error occurred: {str(e)}")

def youtube_converter():
    new_title("Youtube Converter discord.gg/nexustools")
    url = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter the YouTube URL: ")
    file_type = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter 'mp3' for audio or 'mp4' for video: ")
    download_youtube(url, file_type)
    input("Press Enter To continue...")
