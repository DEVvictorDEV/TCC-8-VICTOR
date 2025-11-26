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
        print("teste 1")
        if camera.img_pronta == True:
                print("teste2")
                signal = check.repeat()[6]


        return signal
        


cv2.destroyAllWindows()

