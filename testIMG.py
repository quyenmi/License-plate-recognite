import cv2
from pathlib import Path
import argparse
import time
import glob
from src.lp_recognition import E2E
import pickle
import warnings
warnings.filterwarnings("ignore")

# đổi tên đường dẫn đến file chứa ảnh mỗi file chứa 100-200 ảnh
directory = r"D:\dataset\Minh\ssd\temp"
t = glob.glob(directory + "/*.jpg")
x = glob.glob(directory + "/*.xml")
t.sort()


def create_generator():
	mylist = glob.glob(directory +'/*.jpg')
	for i in mylist:
		yield i

mygenerator = create_generator() # create a generator


data = []
wrong = []
i = 1

for path in mygenerator:
	try:
		# read image
		img = cv2.imread(path)
		# load model
		model = E2E()

		#get license plate character
		lp = model.getchar(img)
		data.append(lp)
		print('Model process on %.d ' %i, path)
		i +=1
	except :
		wrong.append(str(path))
		continue

# comment cái này khi load data nhé
# save data
# mỗi lần chạy nhớ đổi tên nhé VD: car_2.pkl, wrong_2.pkl....
with open('SSS_car7.pkl', 'wb') as fp:
	pickle.dump(data, fp)
	fp.close()

with open('SSD_wrong7.pkl', 'wb') as fp:
	pickle.dump(wrong, fp)
	fp.close()


print(len(wrong))
print(len(t))
print(len(x))

# # dùng để đọc phải đã lưu
# # Load data
# with open("car_6.pkl", "rb") as fp:
# 	test1 = pickle.load(fp)
# 	fp.close()

# print(len(test1))
# # for i in test1:
# # 	print(i)

# with open("wrong_6.pkl", "rb") as fp:
# 	wrong = pickle.load(fp)
# 	fp.close()


# print(len(wrong))