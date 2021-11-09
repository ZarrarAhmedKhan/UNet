from data import *
from model import *
from config import *


train_gen = trainGenerator(batch_size, train_path, image_folder, mask_folder, augm,save_to_dir = output_aug)
print(train_gen)


if os.path.exists(save_weights_path):
  print("using pretrained weights ...")
  pretrained_weights = save_weights_path
else:
  print("No pre trained weights exists !!!")
  pretrained_weights = None

# pretrained_weights = None
model = unet(pretrained_weights = pretrained_weights)
model_checkpoint = ModelCheckpoint(weights_name, monitor='loss',verbose=1, save_best_only=True)

# print("stop")
model.fit_generator(train_gen,steps_per_epoch=steps_per_epoch,epochs=epochs,verbose = 1,callbacks=[model_checkpoint])

model.save(weights_name)
# testGene = testGenerator(test_images_path)
# num_image = 1000
# results = model.predict_generator(testGene,1000,verbose=1)

# saveResult(save_weights_path,results)