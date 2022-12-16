from pytube import YouTube



def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
    #Location to save videos
        youtubeObject.download(output_path='downloads/ytFolder')
    except:
    #Error
        print("An error has occurred")
    print("Download is completed successfully")
    

links = ["https://www.youtube.com/watch?v=1C9jT5J20Ko"]
for i in range(len(links)):
  Download(links[i])