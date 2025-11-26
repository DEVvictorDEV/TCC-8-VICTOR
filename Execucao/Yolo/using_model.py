
import matplotlib as mt
from ultralytics import YOLO
tudo = []

def analise_modelo():
    global results
    model = YOLO('C:/Users/victo/Documents/GitHub/TCC_prototipo/runs/detect/modelo_abc_6_aug/weights/best.pt')

    #caminho da imagem se for usar
    #image_path = 'C:/Users/Gustavo/Desktop/yolo TCC/teste.jpg'

    # ("source="fonte da imagen/video/webcam(0), "show="mostrar o video("Q pra sair"), save="salvar ou nao o video/imagen, "conf="nivel de confianca ajustavel)
    #results = model.predict(source='0', show=True, save=True, conf=0.5)
    results = model.predict(source='C:/Users/victo/Documents\GitHub/TCC_prototipo/datasets/regua.jpeg', show=True, save=True, conf=0.5)

    print("PRINT",results)    
    tudo == results
    
analise_modelo()