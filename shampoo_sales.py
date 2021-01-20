# Inizializzo una lista vuota per salvare i valori
total_values = []
<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 1bd6298262c0ecdba8223b2b33c7f9f7c71dcbbc
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
<<<<<<< HEAD

=======
=======

my_file = open("shampoo_sales.csv", "r")
for line in my_file:

    elements = line.split(',')

    if elements[0] != 'Date':

        date = elements[0]
        value = elements[1]

>>>>>>> 71436b2d408f5c5cdb95446e431eec4e5a72f800
>>>>>>> 1bd6298262c0ecdba8223b2b33c7f9f7c71dcbbc
        total_values.append(float(value))

print(total_values)

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 1bd6298262c0ecdba8223b2b33c7f9f7c71dcbbc
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
<<<<<<< HEAD

=======
=======
>>>>>>> 1bd6298262c0ecdba8223b2b33c7f9f7c71dcbbc
def somma_lista (numeri):
    somma = 0
    for numero in numeri:
        somma = somma + numero    
    return somma

print("Somma :{}".format(somma_lista(total_values)))
<<<<<<< HEAD
=======
>>>>>>> 71436b2d408f5c5cdb95446e431eec4e5a72f800
>>>>>>> 1bd6298262c0ecdba8223b2b33c7f9f7c71dcbbc
