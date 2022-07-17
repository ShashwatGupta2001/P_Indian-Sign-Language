# from moviepy.editor import VideoFileClip
# clip = VideoFileClip("my_video.mp4")
# print( clip.duration )

# SAVE_PATH = "C:/Users/gupta/OneDrive - IIT Kanpur/Shared/ScrapedISL2/" #to_do

# for filename in os.listdir(SAVE_PATH):
#     try: 
#         clip=VideoFileClip(SAVE_PATH+filename)
#         print(filename + " | "+ (clip.duration))
#     except Exception as e: 
#         file_dur = open('Videos_DurErr.csv', 'a+', newline ='')

#         # writing the data into the file
#         with file_dur:	
#             write = csv.writer(file_dur)
#             write.writerows([[filename,str(e)]])    
# print('Task Completed!') # display this message once this task is completed


import os
import csv
import cv2

for filename in os.listdir(SAVE_PATH):
    try: 
        video = cv2.VideoCapture(filename)
        duration = video.get(cv2.CAP_PROP_POS_MSEC)
        
        # #fps = video.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        # #frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        # #duration = frame_count/fps
        print(filename + " | "+ str(duration))
    except Exception as e: 
        file_dur = open('Videos_DurErr.csv', 'a+', newline ='')

        # writing the data into the file
        with file_dur:	
            write = csv.writer(file_dur)
            write.writerows([[filename,str(e)]])    
print('Task Completed!') # display this message once this task is completed