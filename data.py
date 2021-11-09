from augmentor import data_augmentor
<<<<<<< HEAD
import numpy as np
import skimage.io as io
import os
import skimage.transform as trans
import cv2
=======


>>>>>>> 150aec0dbca4518933e6da9e1357e8e82b8c2f12

def adjustData(img,mask):

    if(np.max(img) > 1):
        img = img / 255
        mask = mask /255
<<<<<<< HEAD
        # mask[mask > 0.5] = 1
        # mask[mask <= 0.5] = 0
    return (img,mask)


def trainGenerator(batch_size,train_path,image_folder,mask_folder,augm = False,image_color_mode = "rgb",
                    mask_color_mode = "rgb",image_save_prefix  = "image",mask_save_prefix  = "mask",
=======
        mask[mask > 0.5] = 1
        mask[mask <= 0.5] = 0
    return (img,mask)


def trainGenerator(batch_size,train_path,image_folder,mask_folder,augm = False,image_color_mode = "grayscale",
                    mask_color_mode = "grayscale",image_save_prefix  = "image",mask_save_prefix  = "mask",
>>>>>>> 150aec0dbca4518933e6da9e1357e8e82b8c2f12
                    flag_multi_class = False,num_class = 2,save_to_dir = None,target_size = (256,256),seed = 1):
    '''
    can generate image and mask at the same time
    use the same seed for image_datagen and mask_datagen to ensure the transformation for image and mask is the same
    if you want to visualize the results of generator, set save_to_dir = "your path"
    '''
    # if augm == True:
    	# image_datagen = ImageDataGenerator(**aug_dict)
<<<<<<< HEAD
    image_datagen = data_augmentor()
    mask_datagen = data_augmentor()
=======
	image_datagen = data_augmentor()
	mask_datagen = data_augmentor()
>>>>>>> 150aec0dbca4518933e6da9e1357e8e82b8c2f12
	
    image_generator = image_datagen.flow_from_directory(
        train_path,
        classes = [image_folder],
        class_mode = None,
        color_mode = image_color_mode,
        target_size = target_size,
        batch_size = batch_size,
        save_to_dir = save_to_dir,
        save_prefix  = image_save_prefix,
        seed = seed)
    mask_generator = mask_datagen.flow_from_directory(
        train_path,
        classes = [mask_folder],
        class_mode = None,
        color_mode = mask_color_mode,
        target_size = target_size,
        batch_size = batch_size,
        save_to_dir = save_to_dir,
        save_prefix  = mask_save_prefix,
        seed = seed)
    train_generator = zip(image_generator, mask_generator)
    for (img,mask) in train_generator:
        img,mask = adjustData(img,mask)
        yield (img,mask)

<<<<<<< HEAD
def preprocessed(image,target_size = (256,256),flag_multi_class = False,as_gray = False):
    # image = []
    # for i in range(1,num_image):
    # img = io.imread(os.path.join(image,"%d.jpg"%i))
    # print(img.shape)
    img = image / 255
    img = trans.resize(img,target_size)
    # print(img.shape)
    # img = np.reshape(img,img.shape+(1,)) if (not flag_multi_class) else img
    img = np.reshape(img,(1,)+img.shape)
    # print(img.shape)
    # image.append(img)
    return img



def labelVisualize(num_class,color_dict,img):
    img = img[:,:,0] if len(img.shape) == 3 else img
    img_out = np.zeros(img.shape + (3,))
    for i in range(num_class):
        img_out[img == i,:] = color_dict[i]
    return img_out / 255


def saveResult(i, save_path,original_image, pred_mask, original_mask,flag_multi_class = False,num_class = 2):
    # for i,item in enumerate(npyfile):
    # print("item: ", item.shape)
    # output_image = labelVisualize(num_class,COLOR_DICT,item) if flag_multi_class else item[:,:,0]
    # input_image = input_images[i]
    original_image = (original_image * 255).squeeze()
    pred_mask = (pred_mask * 255).squeeze()
    original_mask = (original_mask * 255).squeeze()

    # print(original_image.shape)

    result_image = np.hstack((original_image,pred_mask,original_mask))
    cv2.imwrite(save_path + '/'+str(i) + '.png', result_image)
    # io.imsave(os.path.join(save_path,"%d_predict.png"%i),img)
=======
def testGenerator(test_path,num_image = 30,target_size = (256,256),flag_multi_class = False,as_gray = True):
    for i in range(num_image):
        img = io.imread(os.path.join(test_path,"%d.png"%i),as_gray = as_gray)
        img = img / 255
        img = trans.resize(img,target_size)
        img = np.reshape(img,img.shape+(1,)) if (not flag_multi_class) else img
        img = np.reshape(img,(1,)+img.shape)
        yield img
>>>>>>> 150aec0dbca4518933e6da9e1357e8e82b8c2f12
