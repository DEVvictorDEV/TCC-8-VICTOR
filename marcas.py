from Yolo import using_model_boxes


def leitura_marcas():
  Classes = using_model_boxes.analise_caixa()
  m_a = False
  m_b = False
  m_c = False
  m_d = False
  m_e = False
  m_f = False
    

  for classe in Classes:
    if classe == "A":
      m_a = True
 
    if classe == "B":
      m_b = True
    if classe == "C":
      m_c = True
 
    if classe == "D":
      m_d = True
 
    if classe == "E":
      m_e = True
 
    if classe == "F":
      m_f = True
 
    #print("A:",m_a,"B:",m_b,"C:",m_c,"D:",m_d,"E:",m_e,"F:",m_f)
  return m_a, m_b, m_c, m_d, m_e, m_f
 
