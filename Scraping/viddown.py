# importing the module 
from pytube import YouTube 
# where to save 
SAVE_PATH = "C:/Users/gupta/OneDrive - IIT Kanpur/Shared/ScrapedISL2/" #to_do 

# importing csv module
import csv
import time

resume = 1762  # define the resume variable in case the download fails

# csv file name
filename = "Videos.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting each datat row one by one
    i=0
    # extracting each data row one by one
    for row in csvreader:
        i+=1
        if i<=resume:
            continue
        print(str(i)+"/3627")
        name = row[0]
        url = row[1]
        identity=row[2]

        # print(url)
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = YouTube(url) 
        except Exception as e: 
            print(url + " | Connection Error : " + str(e)) #to handle exception

        # filters out all the files with "mp4" extension 
        mp4files = yt.streams.filter(file_extension='mp4') 
        
        #to set the name of the file
        #yt.set_filename('GeeksforGeeks Video')  
        
        # get the video with the extension and
        # resolution passed in the get() function 
        #d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
        # print(*mp4files, sep = "\n")
        stream = yt.streams.get_by_itag(18)
        try: 
            # downloading the video 
            stream.download(filename=(str(i)+"_"+ name+".mp4"),output_path=SAVE_PATH) 
        except Exception as e: 
            print(url + " | Error : " + str(e)) #to handle exception
            
            # opening the csv file in 'w+' mode
            file_missed = open('Videos2.csv', 'a+', newline ='')

            # writing the data into the file
            with file_missed:	
                write = csv.writer(file_missed)
                write.writerows([[name,url,identity]])

print('Task Completed!') # display this message once this task is completed


#
# 2605 onwards
#