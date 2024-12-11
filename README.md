# U-Net Segmentation

The basic idea behind the U-Net architecture is to spatially reduce the image feature map size so that the network stores only important features and discards less useful data, and then restores it to its original size, creating a bottleneck for learning important features.
<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*0qJdnSxkerwZPCWVdLPpHw.png" width="700">

</p>

This network architecture consists of a contracting path (left side) and an expansive path (right side). The contracting path follows a typical convolutional network architecture. It consists of iterative applications of two 3x3 convolutions (unpadded convolutions); each is followed by a rectified linear unit (ReLU) and a 2x2 max pooling operation for downsampling, using stride 2. In each downsampling step, we double the number of feature channels. Each step in the expansive path starts with upsampling the feature map, followed by a 2x2 convolution (“up-convolution”) that halves the number of feature channels; then we merge the appropriately cropped feature map from the contracting path, and apply two 3x3 convolutions, each followed by a ReLU. Cropping is necessary because each convolution loses border pixels. In the last layer, a 1x1 convolution is used to map each 64-component feature vector to the desired number of classes. There are 23 convolutional layers in the network in total. In order to tile the output segmentation map smoothly, it is important to choose the input tile size correctly so that all 2x2 max-pooling operations can be applied to a layer with even x and y dimensions.

## Requirements
- Dataset images which we want to segment.
- Black and white masks of datasets which created for every each images. (If the dataset and masks are in the same folder, you need to separate these data with the `mask_sep.py` code.)
- Any code editor and development tools for python code.
- Python libraries: `os`, `shutil`, `torch`, `torch`, `tqdm`, and `matplotlib`

## Features
- The U-Net network stores only important features and discards less useful data.
- U-Net helps to precisely identify objects, boundaries, and contours, making it important for medical imaging, autonomous vehicles, and satellite image analysis.
- Python-based implementation for ease of use and customization.
- Dockerized environment for easy deployment across different systems.

## Usage

This network structure has some stages and it can definable with python codes step by step. 

### Step 1: Definition of U-Net Parts

There are 3 basic building block operations to use the Unet structure. We need to introduce the double convolution, down sample and up sample stages in this step and make them ready for use in the next step.

#### 1.1 DOUBLE CONV

• `__init__` : Sets the number of incoming and outgoing channels with in_channels and out_channels. self.conv_op consists of a nn.Sequential block with two Conv2d and ReLU layers inside.
<br>
<br>
• `forward` : Passes the input x through two convolutions and two ReLUs with the self.conv_op(x) operation and returns the result.
<br>

#### 1.2 DOWN SAMPLE
• `__init__` : self.conv uses DoubleConv; self.pool halves the size with MaxPool2d of 2x2.
<br>
<br>
• `forward` : down = self.conv(x) extracts the basic features, p = self.pool(down) halves the size. down and p are returned as output.
<br>
#### 1.3 UP SAMPLE
• `__init__` : self.up upsamples with ConvTranspose2d; self.conv performs DoubleConv operation on post-upsampling and concatenated channels.
<br>
<br>
• `forward` : x1 is upsampled, x1 and x2 are concatenated, and DoubleConv is applied to return.
<br>

<p align="center">
<img src="https://github.com/user-attachments/assets/cf78d8bb-1cc5-4276-bc4a-c9b303f281f4">
<img src="https://github.com/user-attachments/assets/d895606e-8adb-4652-be9a-931a7a2f51a1">
<img src="https://github.com/user-attachments/assets/0934c776-e001-41a4-9d35-5c43c7f2f85e">
</p>

### Step 2: Creation of U-Net Network Model

This is the step where we build the entire structure on the code using the U-Net building blocks we defined in step 1. We create the U-Net model by following the visually shaped step.
<p align="center">
<img src="https://github.com/user-attachments/assets/86c61b74-8df6-4ca4-adbf-ab462d3875aa">
</p>



### Step 3: Definition of Datasets




## License
MIT
