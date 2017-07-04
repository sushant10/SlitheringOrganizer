import os
#C:\Users\Sushant\Dropbox\College\Summer 17\Python\SlitheringMover

#extract extensions from an external file
#extract directories from an external file
#figure out how to organize college lecture pdf and ppt

#directory's and exclusions
downloads_dir= "C:\Users\Sushant\Downloads";
images_dir="C:\Users\Sushant\Downloads\Slither_organized\Pictures\\";
setup_dir="C:\Users\Sushant\Downloads\Slither_organized\Setup Files\\";
music_dir="C:\Users\Sushant\Downloads\Slither_organized\Music\\";
video_dir="C:\Users\Sushant\Downloads\Slither_organized\Videos\\";
college_dir="C:\Users\Sushant\Dropbox\College\To_be_organized\\";
folders_dir="C:\Users\Sushant\Downloads\Slither_organized\Folders\\";
others_dir="C:\Users\Sushant\Downloads\Slither_organized\Other\\"
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
			os.rename(ogfile_loc,newdir+file)
		except WindowsError:
			pos=file.find('.')
			newfile=file[:pos]+"_dupl"+file[pos:]
			os.rename(ogfile_loc,newdir+newfile)

def main_func():
	down_dic=getallfiles(downloads_dir)
	allfiles={}
	allfiles[images_dir]=file_extension_split([".png",".jpg",".gif",".tif",".bmp",".jpeg"],down_dic)
	allfiles[setup_dir]=file_extension_split([".exe",".inf",".msi"],down_dic)
	allfiles[music_dir]=file_extension_split([".mp3",".wav",".aac",".flac"],down_dic)
	allfiles[video_dir]=file_extension_split([".mp4",".avi",".flv",".wmv",".mov"],down_dic)
	allfiles[folders_dir]=no_extension(down_dic)
	for dir_file,ext_dic in allfiles.iteritems():
		moveto(ext_dic,dir_file) 
	
