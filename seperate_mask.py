from os import listdir
from numpy import asarray
from numpy import vstack
import cv2
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed
 
# load all images in a directory into memory
# size(height, width)
def load_images(path,dest_img, dest_mask, size=(256,512)):
	# src_list, tar_list = list(), list()
	# enumerate filenames in directory, assume all are images
	for filename in listdir(path):
		# print('filename', filename)
		# load and resize the image
		pixels = load_img(path + filename, target_size=size)
		# convert to numpy array
		pixels = img_to_array(pixels)
		# split into satellite and map
		# pixels[height, width]
		sat_img, map_img = pixels[:, :256], pixels[:, 256:]
		cv2.imwrite(f'{dest_img}{filename}', sat_img)
		cv2.imwrite(f'{dest_mask}{filename}', map_img)
		# print("done")
		# break
		# src_list.append(sat_img)
		# tar_list.append(map_img)
	# return [asarray(src_list), asarray(tar_list)]
	print("images and masks are seperated successfully")
 
# dataset path
path = 'maps/val/'
dest_img = 'maps/results/test/images/'
dest_mask = 'maps/results/test/masks/'
# load dataset
print("images and masks are seperating in their respective folders ...")
load_images(path, dest_img, dest_mask)
# print('Loaded: ', src_images.shape, tar_images.shape)
# save as compressed numpy array
# filename = 'maps_256.npz'
# savez_compressed(filename, src_images, tar_images)
# print('Saved dataset: ', filename)