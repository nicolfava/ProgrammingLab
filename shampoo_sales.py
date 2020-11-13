# Inizializzo una lista vuota per salvare i valori
total_values = []

my_file = open("shampoo_sales.csv", "r")
for line in my_file:

    elements = line.split(',')

    if elements[0] != 'Date':

        date = elements[0]
        value = elements[1]

        total_values.append(float(value))

print(total_values)

def somma_lista (numeri):
    somma = 0
    for numero in numeri:
        somma = somma + numero    
    return somma

print("Somma :{}".format(somma_lista(total_values)))