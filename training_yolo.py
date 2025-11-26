# training

from ultralytics import YOLO

#print ("teste")

model = YOLO('yolov8s.pt')

model.train(
    data='E:/Projetos/TCC_prototipo/Execucao/Yolo/data.yaml',
    epochs=50,
    imgsz=640,
    batch=16,
    name='modelo_abc_6_no_aug',
    augment=False
)


#yolo task=detect mode=train model=yolov8s.pt data=data.yaml epochs=50 imgsz=640


#???
