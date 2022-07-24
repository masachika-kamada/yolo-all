# 複数バージョンでのYOLOの性能比較

以下のリポジトリのプログラムを使用し、複数バージョンのYOLOの性能比較を実施

* [YOLOv3](https://github.com/AlexeyAB/darknet)
* [YOLOv4](https://github.com/AlexeyAB/darknet)
* [YOLOv5](https://github.com/ultralytics/yolov5)
* [YOLOv6](https://github.com/meituan/YOLOv6)
* [YOLOv7](https://github.com/WongKinYiu/yolov7)

## 学習条件

* データセット：[BCCD](https://public.roboflow.com/object-detection/bccd/4)
* epochs：100
* batch size：16

## 学習結果

![YOLO結果](https://user-images.githubusercontent.com/63488322/180646684-041dd9b3-050d-4b89-8731-6e3f3ceea60c.png)

## 性能比較

| モデル | mAP@0.5 | 処理時間[msec] |
| :----: | :---: | :--: |
| YOLOv3 | 0.796 | 29.4 |
| YOLOv4 | 0.857 | 35.8 |
| YOLOv5 | 0.854 | 12.1 |
| YOLOv6 | 0.859 |  7.8 |
| YOLOv7 | 0.874 |  9.8 |
