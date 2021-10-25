from data import *
from model import *

batch_size = 2
train_path = 'maps/results/train'
augm = True
image_folder = 'images'
mask_folder = 'masks'
myGene = trainGenerator(batch_size, train_path, image_folder, mask_folder, augm,save_to_dir = None)

pretrained_weights = None
model = unet(pretrained_weights = pretrained_weights)
model_checkpoint = ModelCheckpoint('unet_maps.h5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=300,epochs=1,callbacks=[model_checkpoint])

testGene = testGenerator("maps/results/test/images")
results = model.predict_generator(testGene,30,verbose=1)

saveResult("maps/results/test.output",results)