#ESERCITAZIONE 19/01/21
import re
pattern_float = '\d+\.\d+'
pattern_int = '\d+'


class ExamException(Exception):
    pass

class Diff:
    def __init__(self,ratio = 1):
        self.ratio = ratio

        if not isinstance(self.ratio,int) and not isinstance(self.ratio,float):
            raise ExamException('ERRORE, il ratio deve essere un valore numerico')
        
        if self.ratio <= 0:
            raise ExamException('ERRORE, il ratio deve essere positivo')

    def compute(self,lista_val):
        diff_list = []
        
        if not isinstance(lista_val, list):
            raise ExamException ('ERRORE, la funzione prende in input una lista')        

        if len(lista_val) <= 1:
            raise ExamException ('ERRORE, la funzione non prende in input liste vuote')

        for x in lista_val:
                    if isinstance(x, str):
                        if re.match(x,pattern_float):
                            x = float(x)
                        
                        elif re.match(x,pattern_int):
                            x = int(x)
                        
                        else:
                            raise ExamException ('ERRORE, gli elementi della lista devono essere numerici')
                    
                    if not isinstance(x, int) and not isinstance(x, float):
                        raise ExamException ('ERRORE, la funzione accetta valori numerici o stringhe contenenti numeri')
        
        for x in lista_val[1:]:
            dif = (x - lista_val[(lista_val.index(x)-1)])/self.ratio   
            diff_list.append(dif)

        return diff_list


#    corpo del programma    #
diff = Diff()
result = diff.compute([2,4,8,16])
print(result) # Deve stampare a schermo [2,4,8]
