def somma_lista (numeri):
    somma = 0
    for numero in numeri:
        somma = somma + numero    
    return somma

print("Somma :{}".format(somma_lista([104,4,-6-32])))