'''

#credit: https://stackoverflow.com/questions/35842873/is-there-a-way-to-download-a-video-from-a-webpage-with-python


def download_video(url, num):
    import requests
    #local_filename = url.split('/')[-1]
    if type(num) is int:
      num = str(num)
    local_filename = num+".mp4"
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename
'''

#credit: https://stackoverflow.com/questions/30953104/download-video-from-url-in-python/40553400

import os
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
      self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
      self.savedPath = os.getcwd()
      os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
      os.chdir(self.savedPath)



def download_video(url, num):
    num = str(num)
    import urllib.request
    with cd("clips"):
      urllib.request.urlretrieve(url,num+".mp4") 
      
      


def combinevideo(num_of_clips):
	try:
		from moviepy.editor import VideoFileClip, concatenate_videoclips
	except:
		import os
		os.system("pip install moviepy")
		from moviepy.editor import VideoFileClip, concatenate_videoclips
	clips =[]

	with cd("clips"):
		for i in range(1, num_of_clips+1):
			clips.append(VideoFileClip(str(i)+".mp4"))
	combined = concatenate_videoclips(clips)
	combined.write_videofile("finalvideo.mp4")

