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

### Step 1: Definition of U-Net Parts (unet_parts_1.py)

There are 3 basic building block operations to use the Unet structure. We need to introduce the double convolution, down sample and up sample stages in this step and make them ready for use in the next step.

<p align="center">
  <img src="https://github.com/user-attachments/assets/cf78d8bb-1cc5-4276-bc4a-c9b303f281f4">

  <img src="https://github.com/user-attachments/assets/d895606e-8adb-4652-be9a-931a7a2f51a1">

  <img src="https://github.com/user-attachments/assets/0934c776-e001-41a4-9d35-5c43c7f2f85e">

</p>

#### 1.1 DOUBLE CONV

- `Double Convolution`: Applying two consecutive convolutions instead of a single convolution layer increases the learning capacity. The first convolution extracts low-level features (edges, corners), while the second convolution learns more complex structures.

- `Activation Functions`: ReLU reduces negative values ​​to zero, allowing the model to learn nonlinear relationships.

- `Channel Size`: The first convolution converts the number of channels from in_channels to out_channels. The second convolution preserves this size.

#### 1.2 DOWN SAMPLE
- `Double Convolution`: Low-level features in the input data are made more complex by two consecutive convolutions. This allows the model to learn more detailed structures in the image.

- `Max Pooling (Dimensionality Reduction)`: It reduces the input size by half:

  i) Height and width: (H,W)→(H/2,W/2)

  ii) Number of channels does not change, i.e. the same out_channels are kept.

Pooling process compresses the overall representation while preserving the local information of the image.

- `Double Output (Skip Connections)`:

  i) down (Feature Maps): These are detailed features extracted in the encoder section and then transferred to the decoder with skip connections.
  
  ii) p (Subsampled Maps): Allows the model to learn the lower resolution representation and becomes the input for the next encoder layers.

#### 1.3 UP SAMPLE

- `Convolution Transpose 2D (Upsampling)`: Its purpose is to increase the size of the feature map (usually by a factor of 2). Upsampling expands each pixel in the input and increases the size by minimizing data loss.

- `Concatenate`: Its purpose is to preserve the contextual information by combining the information between the encoder and decoder. The high-resolution detailed information (x2) from the encoder is combined with the large-scale contextual information (x1) from the decoder.

- `Double Convolution`: Its purpose is to learn more complex and rich features by processing the combined feature maps. Since the number of channels is doubled after the concatenation process (e.g. out_channels * 2), convolution processes this high-dimensional data.

<p align="center">
  <img src="https://github.com/user-attachments/assets/cf78d8bb-1cc5-4276-bc4a-c9b303f281f4">

  <img src="https://github.com/user-attachments/assets/d895606e-8adb-4652-be9a-931a7a2f51a1">

  <img src="https://github.com/user-attachments/assets/0934c776-e001-41a4-9d35-5c43c7f2f85e">

</p>

### Step 2: Creation of U-Net Network Model (unet_2.py)

This is the step where we build the entire structure on the code using the U-Net building blocks we defined in step 1. We create the U-Net model by following the visually shaped step.
<p align="center">
<img src="https://github.com/user-attachments/assets/86c61b74-8df6-4ca4-adbf-ab462d3875aa">
</p>

### Step 3: Definition of Datasets (dataset_3.py)
This code is where we access the path of our datasets and masks in the data folder and prepare the input dimensions of the images that will be processed in the UNet model. This code is necessary for us to train our dataset before the main code, which will achieve our main goal. We need to make the necessary definitions here properly.

### Step 4: The Main (main.py)
The definitions required for the training we will do on the Unet model are made in this section. We determine the learning rate, batch size and epoch number of the training. We also define ways to save the data and model. Then we create our training via cuda or cpu. During training, we can also determine the train and valid values ​​through this code.

<p align="center">
<img src="https://github.com/user-attachments/assets/044945a7-f883-4952-8615-527dd9fdd031" width="300">
</p>

### Step 5: Inference (inference.py)
This is the stage that allows us to see the result of the original single photo that we have specified in bulk or path through this training model. The results of my model with only 2 epochs and 1 batch size, which was trained for testing purposes, are as follows. Although this result is quite insufficient for real applications, in appropriate systems and environments, by developing the values ​​in training with these steps, reductions in loss values ​​can be achieved and more usable applications can be developed.

<p align="center">
<img src="https://github.com/user-attachments/assets/e7acd3e7-2065-41f7-88bb-7991aec8d7e6" width="500">
</p>




## License
MIT
