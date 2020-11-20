# Inizializzo una lista vuota per salvare i valori
total_values = []
# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r")
for line in my_file:
# Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
# Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
# Setto la data e il valore
        data = elements[0]
        value = elements[1]
# Aggiungo alla lista dei valori questo valore
        total_values.append(float(value))

print(total_values)

#Definizione della funzione somma
def somma_lista (lista_numeri):
#Inizializzo una variabile dove salvare la somma
    somma = 0
#Sommo ogni elemento della lista
    for item in lista_numeri:
        somma = somma + item   
    print("Somma :{}".format(somma))

#Stampo il risultato della somma di tutti i valori della lista
somma_lista(total_values)
