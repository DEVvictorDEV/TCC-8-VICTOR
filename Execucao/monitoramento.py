import marcas
import time

def monitoramento():
    m_a, m_b, m_c, m_d, m_e, m_f = marcas.leitura_marcas() 
    #if m_regua is True:
          #print("regua reconhecida")
 
    a_sub ,b_sub, c_sub, d_sub , e_sub, f_sub = False,False,False,False,False,False;
 
    if m_a == False: # A foi submerso
        print("A foi submerso")
        a_sub = True
 
        time.sleep(1)
 
        if m_a | m_b == False: # B foi submerso
            print("B foi submerso")
            b_sub = True
            time.sleep(1)
 
            if  m_a | m_b | m_c == False: # C foi submerso
                print("C foi submerso")
                c_sub = True
 
                time.sleep(1)
 
                if  m_a | m_b | m_c | m_d == False: # d foi submerso
                    print("D foi submerso")
                    d_sub = True
 
                    time.sleep(1)
 
                    if  m_a | m_b | m_c | m_d | m_e == False: # E foi submerso
                        print("E foi submerso")
                        e_sub = True
 
                        time.sleep(1)
 
                        if  m_a | m_b | m_c | m_d | m_e | m_f== False: # F foi submerso
                            print("F foi submerso")
                            f_sub = True
                            time.sleep(1)
 


    print("Embaixo d agua:","A:", a_sub,"B:",b_sub,"C:",c_sub,"D:",d_sub,"E:",e_sub,"F:",f_sub )
    return a_sub, b_sub, c_sub, d_sub, e_sub, f_sub
