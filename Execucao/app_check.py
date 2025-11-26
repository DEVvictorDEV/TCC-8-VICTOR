import threading
import time
import alerta
import camera
import main
import check
import monitoramento
from flask import Flask, render_template
from flask_socketio import SocketIO



# Falta ajustar para ciclos de camera ! ! !

#camera.camera_f()


#camera.camera_f()
"""while camera.quebra == True:
    print(camera.quebra)
    #if check.cond == True:
    camera.camera_f()
    print ("teste 1")
    if camera.img_pronta == True:
            print("teste2")
            #using_model_boxes.analise_caixa()
            #print (using_model_boxes.analise_caixa())
            #print (marcas.leitura_marcas())
            #monitoramento.monitoramento()
            #print (check.repeat())
            ""def  repeat():
                global sinal
                sinal = False

                contador = 0
            
                for i in range(5): # vai fazer 10 checagens se o d_sub esta submerso para não apresentar falsos positivos
                a_sub, b_sub, c_sub, d_sub, e_sub, f_sub = monitoramento.monitoramento()
                #print("mon",monitoramento())
                if c_sub == True:
                    contador += 1
                    print("contador:",contador)
                    time.sleep(1)
                if contador == 5:
                print("alagemento na regiao")
                sinal = True
                print(sinal)
                else:
                c_sub = False
            
                return a_sub, b_sub, c_sub, d_sub, e_sub, f_sub
"""
# -----------------------
# Flask + SocketIO
# -----------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disparar_alerta')
def disparar_alerta():

    # pegar só o setimo valor do return
    sinal = main.main()
    print("vamo ver", sinal)
    if sinal == True:
        print("Emitindo alerta manual")
        #with app.app_context():
        #socketio.emit('alerta', {'mensagem': '🚨 Alerta de alagamento ou enchente na região!'})
    return socketio.emit('alerta', {'mensagem': '🚨 Alerta de alagamento ou enchente na região!'})

# -----------------------
# Thread para alerta automático
# -----------------------
"""def monitorar_alerta():
    while True:
        time.sleep(10)
        if repet():
            print("Emitindo alerta automático!")
            with app.app_context():
                socketio.emit('alerta', {'mensagem': '🚨 Alerta automático: enchente detectada!'})
        else:
            print("Nenhum alagamento detectado.")
"""
# -----------------------
# Execução principal
# -----------------------
if __name__ == '__main__':
    # Inicia câmera em paralelo
   # threading.Thread(target=camera.camera_f, daemon=True).start()
    # Inicia o monitoramento automático em paralelo
    threading.Thread(target=disparar_alerta, daemon=True).start()
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
