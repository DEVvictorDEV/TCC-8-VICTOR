import time
import alerta


contador2 =0
#while True: # a iaeia aqui é tirar 5 fotos diferentes em tempos diferentes e se todas estiverem submersas emite o alerta

def main():  
    while True:  
        global contador2
        s =alerta.sinal_alerta()
        print("s", s)
        if s == True:
            contador2 = contador2 +1
            print("contador2",contador2)
                            
        if contador2 == 2:
            contador2=0
            print("enviar sinal")
            return True

        if s ==False:
            contador2 = 0
            main()

        time.sleep(2)


