import time
import monitoramento
import camera

# Falta ajustar para ciclos de camera ! ! !

def  repeat():
    #global sinal
    sinal = False
 
    contador1 = 0
    #camera.camera_f()
    for i in range(3): # vai fazer 10 checagens se o d_sub esta submerso para não apresentar falsos positivos
      
      a_sub, b_sub, c_sub, d_sub, e_sub, f_sub = monitoramento.monitoramento()
      #print("mon",monitoramento())
      if c_sub == True:
        contador1 += 1
        print("contador:",contador1)
        time.sleep(1)
    if contador1 == 3:
      print("Alagemento na regiao!")
      sinal = True
      print("si",sinal)
    else:
      c_sub = False
 
    return a_sub, b_sub, c_sub, d_sub, e_sub, f_sub, sinal
      #break
