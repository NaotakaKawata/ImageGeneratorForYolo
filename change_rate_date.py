#Python3で実行
import os
import glob
import sys
try:
	sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
	pass
import numpy as np
from sklearn.model_selection import train_test_split
import cv2
abspath = os.path.dirname(os.path.abspath(__name__))
list_data = []
train_data = []
valid_data = []
test_data = []
#目標画像を以下のディレクトリに格納
path = "./data/obj/"
files = os.listdir(path)
file_train = open('train.txt', 'w')
file_valid = open('valid.txt', 'w')
text = ""
for f in files:
	if os.path.isfile(os.path.join(path, f)):
		if f.endswith(".png"):
			list_data.append("data/obj/" + f)

#train = 90%, valid = 10%
#test_sizeを変更する
train_data, valid_data = train_test_split(list_data, test_size = 0.1)
for train in train_data:
	#print (train)
	file_train.write(train + "\n")
for valid in valid_data:
	#print (train)
	file_valid.write(valid + "\n")
