# U-Net: Convolutional Networks for Biomedical Image Segmentation

## Theory

### UNet Arhitecture

[alt text](./pics/UNet architecture.png?raw=true)
UNet is a convolution neural network which is the expanded by few changes in the CNN arhitecture.

UNet is more than image classification. 'UNet is able to localize and distinguish borders is by doing classification on every pixels, so input and output share the same size.'

There is no Dense layer in the UNet. It only contains Convolutional layers and does not contain any Dense layer because of which it can accept image of any size.

UNet has a "U" shape and there are two parts of the UNet arhitecture.
The first one the contracting path (which is consist of general convolutinal process).
The second phase is expansive path (which is constituted by transposed 2d convolutuonal layers) or we can say upsampling of the layers.

Now I will define the both path seperately.

1. Contrcting Path:

This path follow like this

conv_layer1 -> conv_layer2 -> max_pooling -> dropout(optional)

Two conv layers plus max_pooling

In this path , the depth of the convolution layer is increaing and image size is decreaing gradually.

2. Expansive Path:

This path follow like this

conv_2d_transpose -> concatenate -> conv_layer1 -> conv_layer2

Transposed convolution is an upsampling technique that expand the size of the image.
