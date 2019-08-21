#Python3で実行
import os
import glob
import sys
try:
	sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
	pass
import cv2
abspath = os.path.dirname(os.path.abspath(__name__))

#目標画像を以下のディレクトリに格納
list = []
class_list = []
path = "./items/"
folders = os.listdir(path)
file_obj = open('obj.names', 'w')
file_class = open("names.list", "w")
for j, folder in enumerate(folders):
	if os.path.isdir(os.path.join(path, folder)):
		item_path = path + folder + "/"
		#print(item_path)
		files = glob.glob(item_path + "*.png")
		list.append(folder)
		class_list.append("c" + str(j))
	else:
		print("EROOR")
		exit(1)
	for i, f in enumerate(files):
		os.rename(f, os.path.join(item_path, str(j) + '_' + '{0:05d}'.format(i) + "_c" + str(j) + ".png"))

for line in list:
	file_obj.write(line + "\n")

for line in class_list:
	file_class.write(line + "\n")
