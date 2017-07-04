import os
import getpass
import pickle
import json

#Generates text file with dictionary of default directories..
#with keys as directories and values as extensions

base_dir="C:\Users\\"


images_dir= "Downloads\Slither_organized\Pictures\\"
setup_dir="Downloads\Slither_organized\Setup Files\\"
music_dir="Downloads\Slither_organized\Music\\"
video_dir="Downloads\Slither_organized\Videos\\"
college_dir="Downloads\Slither_organized\To_be_organized\\";
folders_dir="Downloads\Slither_organized\Folders\\";
others_dir="Downloads\Slither_organized\Other\\"

all_dir={}
all_dir["Downloads"]= "downloads";
all_dir[images_dir]=[".png",".jpg",".gif",".tif",".bmp",".jpeg"]
all_dir[setup_dir]=[".exe",".inf",".msi"]
all_dir[music_dir]=[".mp3",".wav",".aac",".flac"]
all_dir[video_dir]=[".mp4",".avi",".flv",".wmv",".mov"]
all_dir[college_dir]=[".pdf",".ppt",".pptx"]
all_dir[folders_dir]="folders"
all_dir[others_dir]="others"

#tried using pickle
"""def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
"""

def get_final():
	username= getpass.getuser() +"\\"
	final_dic={}
	for direc,ext in all_dir.iteritems():
		direc=base_dir+username+direc
		final_dic[direc]=ext
	return final_dic


allfiles=get_final()
#save_obj(allfiles, "direc_and_ext")
with open('direc_and_ext.txt', 'w') as file:
        file.write(json.dumps(allfiles))



