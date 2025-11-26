import using_model
import re

from collections import Counter

def contagem():
    global results
    global retorno
    result = using_model.results[0]
    boxes = result.boxes

    # Lista de IDs de classes detectadas
    class_ids = [int(cls) for cls in boxes.cls]

    # Conta quantas vezes cada classe apareceu
    counts = Counter(class_ids)

    # Mapeia para os nomes das classes
    for cls_id, count in counts.items():
        class_name = result.names[cls_id]
        print(f"{class_name}: {count}") #conta a quantidade de vezes de cada classe que aparecem
        retorno = f"{class_name}: {count}"


    return retorno
#contagem()


