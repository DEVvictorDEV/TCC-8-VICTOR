# Testando as funcoes
import cv2
import camera
import marcas
import monitoramento
import check
from Yolo import using_model_boxes
 
camera.quebra = True
 
 
def sinal_alerta():
   
        camera.camera_f()
        if camera.img_pronta == True:
                signal = check.repeat()[6]
 
 
        return signal
       