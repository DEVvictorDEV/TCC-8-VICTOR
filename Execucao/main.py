import time
import alerta

contador2 = 0

def main():
    global contador2

    s = alerta.sinal_alerta()

    if s:
        contador2 += 1
        print("contador_2: ", contador2)

        if contador2 >= 2:  # dispara alerta após 2 detecções seguidas
            contador2 = 0
            print("enviar sinal")
            return True
        else:
            return False

    else:
        contador2 = 0
        return False

    time.sleep(2)