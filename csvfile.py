# oggetto CSV
# - init(filename)
# - name
# - get data()
#      return dati

class CSVFile:
    def __init__(self,name):
            self.name = name
    
    def get_data(self):
        # Inizializzo una lista vuota per salvare i valori
        total_values = []
        # Apro e leggo il file, linea per linea
        my_file = open(self.name, 'r')
        for line in my_file:
        # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')
        # Se NON sto processando l’intestazione...
            if elements[0] != 'Date':
        # Setto la data e il valore
                data = elements[0]
                value = elements[1]
        # Aggiungo alla lista dei valori questo valore
                try:
                    total_values.append(float(value))
                
                except NameError:
                    print('Un valore della lista non è definito')
                except ValueError:
                    print('Un valore non è di tipo "float"')
        
        return total_values


mio_file = CSVFile(name = 'shampoo_sales.csv')

print(mio_file.name)
print(mio_file.get_data())