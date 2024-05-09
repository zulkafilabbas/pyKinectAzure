# pyKinectAzure
[![PyPI](https://img.shields.io/pypi/v/pykinect-azure?color=2BAF2B)](https://pypi.org/project/pykinect-azure/)

![Azure kinect color and depth combination](https://github.com/ibaiGorordo/pyKinectAzure/blob/master/doc/images/outputImage.jpg)

Python 3 library for the Azure Kinect DK sensor-SDK.

## Similar solutions
Part of the ideas in this repository are taken from following repositories:
* [pyk4a](https://github.com/etiennedub/pyk4a): Really nice and clean Python3 wrapper for the Kinect Azure SDK.

* [Azure-Kinect-Python](https://github.com/hexops/Azure-Kinect-Python): More complete library using ctypes as in this repository, however, examples about how to use the library are missing and the library is harder to use.

The objective of this repository is to combine the strong points of both repositories by creating a easy to use library that allows the use of most of the functions of the Kinect Azure. Also, to create sample programs to showcase the uses of the library

## Prerequisites
* [Azure-Kinect-Sensor-SDK](https://github.com/microsoft/Azure-Kinect-Sensor-SDK): required to build this library.
  To use the SDK, refer to the installation instructions [here](https://github.com/microsoft/Azure-Kinect-Sensor-SDK).
* **ctypes**: required to read the library.
* **numpy**: required for the matrix calculations
* **opencv-python**: Required for the image transformations and visualization.

## Installation
```commandline
pip install pykinect_azure
```
The above will install pykinect_azure (official) 0.0.3 (as of 10/5/2024), if you want to install this version instead,
```commandline
cd your_repo/
git clone https://github.com/zulkafilabbas/pyKinectAzure.git
conda create -n whl_env python=3.10.13
conda activate whl_env
conda install pip
pip install setuptools wheel
python setup.py bdist_wheel
cd your_repo/dist/
pip install <this_package>.whl
```

## How to use this library

* The original library was **tested in Windows 10 and Ubuntu 20.04** with the Kinect Azure SDK 1.4.0 and 1.4.1.
* This fork was tested has been **tested on Windows 11 (latest updates - as of 10/5/2024), Windows 10 (latest updates - as of 10/5/2024), Kinect Azure SDK v1.4.1, Body Tracking SDK v1.1.2, DK Firmware 1.6.110079014, Nvidia 1660Ti GPU (Desktop), Nvidia 1650 GPU (Laptop), Nvidia 4060 GPU (Laptop)**

  - **Windows:** When using the pyKinectAzure class, it requires the **path to the k4a.dll module**, make sure that the path is the correct one for your Kinect Azure SDK version. By default the path (**module_path**) is set to  ```C:\\Program Files\\Azure Kinect SDK v1.4.0\\sdk\\windows-desktop\\amd64\\release\\bin\\k4a.dll```.

  - **Linux:** When using the pyKinectAzure class, it requires the **path to the k4a.so module**, make sure that the path is the correct one for your Kinect Azure SDK version. When using Linux set **module_path** to  ```/usr/lib/x86_64-linux-gnu/libk4a.so```, please follow the [instruction](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/docs/usage.md) from microsoft to install the right packages.
  
   - **Nvidia Jetson:** When using the pyKinectAzure class, it requires the **path to the k4a.so module**, make sure that the path is the correct one for your Kinect Azure SDK version. When using Nvidia Jetson set **module_path** to to  ```'/usr/lib/aarch64-linux-gnu/libk4a.so'```, please follow the [instruction](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/docs/usage.md) from microsoft to install the right packages.

* The **pyKinectAzure** class is a wrapper around the **_k4a.py** module to make the library more understandable. However, the **pyKinectAzure** class still contains few methods from the Kinect Azure SDK

* The **_k4a.py** module already contains all the methods in the Kinect Azure SDK. So, for more advanced of the Kinect Azure SDK check the **_k4a.py** module.

## Examples
For an example on how to obtain and visualize the depth data from the Azure Kinect DK check the **exampleDepthImageOpenCV.py** script.
```
git clone https://github.com/ibaiGorordo/pyKinectAzure.git
cd pyKinectAzure/examples
python exampleDepthImageOpenCV.py
```

Also, there is an example to obtain and visualize the smooth depth from the Azure Kinect DK check the **exampleSmoothDepthImageOpenCV.py** script.
```
python exampleSmoothDepthImageOpenCV.py
```
> note: when you are dealing on the linux platform, please insure that the user have permission to the usb devices, or always execute under the root permission by adding `sudo` ahead.

![Azure kinect smoothed depth image comparison](https://github.com/ibaiGorordo/pyKinectAzure/blob/master/doc/images/Azure%20kinect%20smoothed%20depth%20image.png)

A debugging test example can be found [here](https://github.com/zulkafilabbas/pyKinectAzure/blob/master/examples/exampleColorImageBodyTracking.py)

## Contribution
Feel free to send pull requests.
Bug reports are also appreciated. Please include as much details as possible.

## TODO:
### Possible additions
- [ ] Audio capture
- [ ] Data streaming wrappers for Kinect & Audio data
- [ ] Remote Heartbeat
- [ ] Extrensic calibration for multiple sensors
- [ ] Body tracking configuration access (Merge from one of the forks)
- [ ] H264/H265 Example
- [ ] ROS-1 Integration
- [ ] ROS-2 Integration

### Features to merge from forks
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/commit/8fc2d1c11cc4b411c6f87df8ae168ef4778bac0c
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/commit/e5cba94d046aeb3e299618d60345c7b9da299680
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...coenarrow:pyKinectAzure:master
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...jancuz:pyKinectAzure:master
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...jonas-hurst:pyKinectAzure:master
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...melung:pyKinectAzure:master
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...orbbec:pyKinectAzure:master
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...ShivinDass:pyKinectAzure:master
- [ ] https://github.com/ibaiGorordo/pyKinectAzure/compare/master...Kami-code:pyKinectAzure:master

### Beyond
- [ ] https://github.com/isarandi/metrabs 
- [ ] https://github.com/zef1611/AIC23_NLRetrieval_HCMIU_CVIP 
- [ ] https://github.com/HiROS-unipd
- [ ] https://github.com/LiheYoung/Depth-Anything 
- [ ] https://github.com/WongKinYiu/yolov9 
- [ ] https://github.com/open-mmlab/mmpose 
- [ ] https://github.com/ifzhang/ByteTrack
- [ ] https://github.com/orbbec/pyKinectAzure


### Wrappers for the Kinect Azure data
- [x] Create wrapper to read depth images.
- [x] Create wrapper to read Infrared images.
- [x] Create wrapper to read IMU data.
- [x] Create function to convert image buffer to image depending on the image type.
- [x] Create wrapper to transform depth image to color image.
- [x] Create wrapper to transform depth image to 3D point cloud.
- [x] Create funtion to visualize 3D point cloud.

### Create examples
- [x] Example to visualize depth images.
- [x] Example to visualize passive IR images.
- [x] Example to plot IMU data.
- [x] Example to visualize Depth as color image.
- [x] Example to overlay depth color with alpha over real image.
- [x] Example to visualize 3D point cloud

### Body tracking
- [x] Create library for the body tracking SDK similar the same way as the current library.
- [x] Combine image and skeleton data.
- [ ] Generate 3D skeleton visualization.

### Future ideas
- [ ] Run Deep Learning models on Kinect data (Openpose 3D skeleton, semantic segmentation with depth, monocular depth estimation validation)
- [ ] Track passive infrared marker for motion capture analysis