from config import *
from data import *
from model import *

if os.path.exists(save_weights_path):
  print("using pretrained weights ...")
  pretrained_weights = save_weights_path
else:
  print("No pre trained weights exists !!!")
  pretrained_weights = None

model = unet(pretrained_weights = pretrained_weights)

if pretrained_weights is None:
  print("exit")
else:
  if not os.path.exists(save_results_path):
    os.mkdir(save_results_path)
  for i in range(1,num_test_images+1):
    img = io.imread(os.path.join(test_images_path,"%d.jpg"%i))
    mask = io.imread(os.path.join(test_mask_path, "%d.jpg"%i))

    original_image = preprocessed(img)
    original_mask = preprocessed(mask)

    pred_mask = model.predict(original_image)
    print(f"predicted {i} ", pred_mask.shape)
    saveResult(i, save_results_path,original_image, pred_mask, original_mask)
    # break