import os
import cv2
from os import listdir
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

def my_datagen(train_path):
	path = train_path + 'images/'
	total_images = len(listdir(path))

	images_path = train_path + 'images/'
	masks_path = train_path + 'masks/'

	images_list = listdir(images_path)
	masks_list = listdir(masks_path)

	X_train = []
	y_train = []

	for i in range(total_images):
		print(i)

		print(train_path + 'images/' + images_list[i])
		print(train_path + 'masks/' + masks_list[i])

		img = load_img(images_path+ images_list[i])
		mask = load_img(masks_path + masks_list[i])

		img = img_to_array(img)
		mask = img_to_array(mask)

		# print(img[0])
		# print(mask.shape)

		img = img / 255.0
		mask = mask / 255.0

		# print("after normalization: ")

		X_train.append(img)
		y_train.append(mask)

		print(len(X_train))

		break


train_path = 'maps/results/train/'
my_datagen(train_path)
print('done')