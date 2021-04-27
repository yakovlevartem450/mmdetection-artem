# MMDetection: Cats and Dogs Breed Object Detection

## Disclaimer
I'm not a CS student, and all of my background is in Econ and Operations Management. Please don't judge harshly if something is not at the level of complexity you expected, it's my first experience with Deep Learning.

## Input/Output
**Input**: Cat/Dog image

**Output**: annotated image of a cat or a dog with a predicted breed and a likelihood score

## Deliverables
 - Preprocessed annotated data after sorting and cleaning (available from the Dropbox link or upon request)
 - Google Colab Notebook with all the instructions and results for demonstration purposes
 - Code for reconfiguring pre-existing models
 - Code for visualizing the performance evaluation 


![](0002.jpg)

### **Solution**: breed identification using object detection

![](0003.jpg)

![](0004.jpg)

**Key Advantages:**

 - **Modular Design**

  We decompose the detection framework into different components and one can easily construct a customized object detection framework by combining different modules.

- **Support of multiple frameworks out of box**

  The toolbox directly supports popular and contemporary detection frameworks, *e.g.* Faster RCNN, Mask RCNN, RetinaNet, etc.

- **High efficiency**

  All basic bbox and mask operations run on GPUs now. The training speed is faster than or comparable to other codebases, including [Detectron](https://github.com/facebookresearch/Detectron), [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) and [SimpleDet](https://github.com/TuSimple/simpledet).

- **State of the art**

  The toolbox stems from the codebase developed by the *MMDet* team, who won [COCO Detection Challenge](http://cocodataset.org/#detection-leaderboard) in 2018, and we keep pushing it forward.
  

![](0006.jpg)

### **Note: good dataset with balanced classes.**
 
![](0005.jpg)

## Installation and Usage

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)] (https://colab.research.google.com/github/maxyakovlevclone/mmdetection/blob/master/mmdetection_pets.ipynb)

### **Note**: Preset Runtime Settings to GPU instead of CPU in the Google Colab. Also please follow the instructions for adjusting the number of training epochs and choosing the model.

All the instructions can be found in the Google Colab Notebook. Please don't hesitate to contact me if you have any questions.

## Performance (Example from Faster-RCNN with 25 training epochs) 
![Exhibit 1. Precision-Recall Table](precision-recall_faster_rcnn.JPG)


![Exhibit 2. Performance in Training](training_performance.png)


![Exhibit 3. AUC and F-Measure Graph](AUC.png)




![](0008.jpg)

![](0009.jpg)

![Exhibit 5. Precise Identification at Angle](prediction.png)


![Exhibit 6. Correct Identification of a Puppy's Breed](prediction_1.png)






## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@article{mmdetection,
  title   = {{MMDetection}: Open MMLab Detection Toolbox and Benchmark},
  author  = {Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and
             Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and
             Liu, Ziwei and Xu, Jiarui and Zhang, Zheng and Cheng, Dazhi and
             Zhu, Chenchen and Cheng, Tianheng and Zhao, Qijie and Li, Buyu and
             Lu, Xin and Zhu, Rui and Wu, Yue and Dai, Jifeng and Wang, Jingdong
             and Shi, Jianping and Ouyang, Wanli and Loy, Chen Change and Lin, Dahua},
  journal= {arXiv preprint arXiv:1906.07155},
  year={2019}
}
```


## Contact

Max Yakovlev - maksim.yakovlev@kellogg.northwestern.edu
