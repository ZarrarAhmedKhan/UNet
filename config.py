total_train_count = 1096
batch_size = 24
epochs = 100
steps_per_epoch = int(total_train_count / batch_size)
train_path = 'data/train'
test_images_path = "data/test/images"
test_mask_path = "data/test/masks"
save_weights_path = 'CheckPoints/unet_map_100.h5'
weights_name = f'CheckPoints/unet_map_{epochs}.h5'
# path_validation = 'data/val_data/'
save_results_path = f'results_{epochs}'

num_test_images = 10

augm = True
output_aug = None

image_folder = 'images'
mask_folder = 'masks'

# model_name = 'CheckPoints/unet_map_50.h5'