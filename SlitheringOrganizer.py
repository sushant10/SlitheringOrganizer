import os
import json
import pickle
#C:\Users\Sushant\Dropbox\College\Summer 17\Python\SlitheringMover

#figure out how to organize college lecture pdf and ppt

#exclude when slithering
exclude=["Slither_organized","Folders","Downloadsdesktop.ini","desktop.ini"]

def getallfiles(loc):
	files= os.listdir(loc);
	file_dic={}
	for file in files:
		if file in exclude: 
			continue;
		file_dic[file]=loc+"\\"+file
	return file_dic 

def file_extension_split(ext,file_dic):
	#file_dic= getallfiles(loc)
	ext_dic={}
	for file,file_loc in file_dic.iteritems():
		pos=file.find('.')
		if file[pos:].lower() in ext :
			ext_dic[file]=file_loc
	return ext_dic

def no_extension(file_dic):
	noext={}
	for file,file_loc in file_dic.iteritems():
		pos=file.find('.')
		if pos == -1:
			noext[file]=file_loc
	return noext

def moveto(og,newdir):
	for file,ogfile_loc in og.iteritems():
		try:
			#print ogfile_loc
			#print "\n"
			#print newdir+file
			os.rename(ogfile_loc,newdir+file)
		except WindowsError:
			pos=file.find('.')
			newfile=file[:pos]+"_dupl"+file[pos:]
			os.rename(ogfile_loc,newdir+newfile)


def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def organize():
	down_dir=""
	others_dir=""
	fromfiles = {}
	#open the file
	#fromfiles= load_obj("direc_and_ext")
	with open("direc_and_ext.txt") as file:
		fromfiles = json.load(file)

	#get downloads directory
	for direc,key in fromfiles.iteritems():
		if key == "downloads":
			down_dir=direc
		if key == "others":
			others_dir=direc 
	
	down_dic=getallfiles(down_dir)
	allfiles={}
	#forming nested dictionary based on extension
	for direc,key in fromfiles.iteritems():
		if key == "downloads" or key == "others" :
			continue 
		if key == "folders" :
			allfiles[direc]=no_extension(down_dic)
		allfiles[direc]=file_extension_split(key,down_dic)

	#moving for most extension
	for dir_file,ext_dic in allfiles.iteritems():
		moveto(ext_dic,dir_file) 
	
	#for moving others
	down_dic=getallfiles(down_dir)
	moveto(down_dic,others_dir)