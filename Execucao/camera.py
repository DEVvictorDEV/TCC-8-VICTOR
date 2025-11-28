import cv2
import time
# Inicia a captura da webcam (0 é a câmera padrão)

quebra = True

def camera_f():
    global quebra
    global img_pronta
   
    quebra = True
    img_pronta = False

    img_pronta = False
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao abrir a webcam.")
        exit()

    #print("Pressione a tecla ESPAÇO para salvar o frame. Pressione ESC para sair.")
    
    while quebra == True:
        ret, frame = cap.read()
        if not ret:
            print("Frame nao capturado.")
            break
        
            

        # Mostra o frame
        cv2.imshow("Webcam", frame) 

        # Espera por tecla (delay de 1ms)
        # tirada de foto manual
        key = cv2.waitKey(1)
        
        if key == 27:  # ESC para sair
            break


        #tirar a foto automaticamente
        time.sleep(5)
        cv2.imwrite("E:/Projetos/TCC_prototipo/Execucao/imagen/frame_salvo.png", frame)
        print("Frame salvo como frame_salvo.png")
        img_pronta = True
        quebra =False
        
    # Libera a webcam e fecha a janela
    cap.release()
    cv2.destroyAllWindows()