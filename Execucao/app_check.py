import threading
import time
import main
import camera
from flask import Flask, render_template
from flask_socketio import SocketIO
 
#def index():
#    return render_template('index.html')
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
 
@app.route('/projeto')
def projeto():
    return render_template('projeto.html')
 
@app.route('/grupo')
def grupo():
    return render_template('grupo.html')
 
@app.route('/disparar_alerta')
def disparar_alerta_route():
    emitir_alerta("MANUAL")
    return "Alerta disparado!"
 
def emitir_alerta(tipo="AUTOMÁTICO"):
    try:
        sinal = bool(main.main())
    except Exception as e:
        print("⚠️ Excecao em main.main():", e)
        sinal = False
 
    if sinal:
        print(f"Emitindo alerta {tipo}")
        socketio.emit('alerta',{'mensagem': f'🚨 Alerta {tipo}: Alagamento ou enchente detectada!'})
 
def monitorar():
    while True:
        emitir_alerta("AUTOMÁTICO")
        time.sleep(10)
 
if __name__ == '__main__':
    socketio.start_background_task(monitorar)
    threading.Thread(target=camera.camera_f, daemon=True).start()
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
