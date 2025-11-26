
import matplotlib as mt
from ultralytics import YOLO
tudo = []

def analise_caixa():
    global results
    Classes = []
    #index = -1
    model = YOLO('C:/Users/victo/Documents/GitHub/TCC_prototipo/runs/detect/modelo_abc_6_aug/weights/best.pt')

    #caminho da imagem se for usar
    #image_path = 'C:/Users/Gustavo/Desktop/yolo TCC/teste.jpg'

    # ("source="fonte da imagen/video/webcam(0), "show="mostrar o video("Q pra sair"), save="salvar ou nao o video/imagen, "conf="nivel de confianca ajustavel)
    #results = model.predict(source='0', show=True, save=True, conf=0.5)
    results = model.predict(source='C:/Users/victo/Documents/GitHub/TCC_prototipo/Execucao/imagen/frame_salvo.png', show=True, save=False, conf=0.5)
    
    for results in results:
        boxes = results.boxes
        for box in boxes:
            cls_id = int(box.cls[0].item())
            class_name = model.names[cls_id]
            #print(f'Classe: {class_name}')
            Classes.append(class_name,)
            #index += 1
    #print("PRINT",results)    
    #tudo == results
    return Classes

#analise_caixa()
#print (analise_caixa())


