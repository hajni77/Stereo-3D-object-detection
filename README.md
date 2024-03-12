# Stereo-3D-object-detection

Research:
https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/lectures/self-driving-cars/
https://paperswithcode.com/search?q_meta=&q_type=&q=stereo+3d+object+detection

https://www.youtube.com/embed/JEVtVrNFb30?index=40&list=PL05umP7R6ij321zzKXK6XCQXAaaYjQbzr
- 2D object det. bounding boxes: 
  - x,y,w,h
- 3D object det bounding boxes:
  - x,y,z,w(idth),h(eight),l(ength),r(oll),p(itch),y(aw)
  - assume zero roll and pitch(driving on the road)
  - difficulty depends on input: 2D image or 3D point cloud
  - detection performance is typically measured using average precision
  - challenges: appearance/viewpoint variations, illuminations, clutter, occlusion
  - two stage detection methods are state-of-art. Faster R-CNN, Mask R-CNN
  - Feature pyramid networks help detecting features at various scale
- 2D images:
  - regressing 3D boxes from monocular images(need good object size priors)
  - stereo information helps to localize the box in 3D space(but quadratic error)

Stereo
simonella iccv 2021
https://paperswithcode.com/paper/fcos-fully-convolutional-one-stage-object
  - 1. predict a depth map
    2. pseudo lidar
    3. standard lidar based detection
       
frustum pointnet 2018
  1. generate 2D proposals in the rgb image
  2. extract point cloud from 3D object frustum
  3. predict 3D bounding box from points in frustum via PointNET

PointNet stages:
  -segmentation of RGB point cloud
  -translation of points such that centroid aligns with 3D box center
  -3D bounding box regression

![image](https://github.com/hajni77/Stereo-3D-object-detection/assets/78812524/60f08378-97b0-4ab5-8a7d-2c0cc2d47d2c)

3DOP

![image](https://github.com/hajni77/Stereo-3D-object-detection/assets/78812524/a6067e1a-3efb-4fa2-8ce0-84094f75abc4)

models:
https://github.com/HKUST-Aerial-Robotics/Stereo-RCNN
https://github.com/megvii-basedetection/bevstereo
https://github.com/Owen-Liuyuxuan/visualDet3D
https://github.com/mileyan/pseudo_lidar
https://towardsdatascience.com/understanding-and-implementing-faster-r-cnn-a-step-by-step-guide-11acfff216b0
https://github.com/swords123/IDA-3D
data
https://arxiv.org/pdf/2004.06320.pdf
