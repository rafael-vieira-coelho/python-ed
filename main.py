
from PesquisaBinaria import binarySearch
from Selecao import selectionSort
from Insercao import insertionSort
from random import shuffle

if __name__ == '__main__':
    numeros = [0, 5, 10, 15, 20]
   # posicao1 = binarySearch(15, numeros)
   # posicao2 = binarySearch(9, numeros)

   # shuffle(numeros)
   # print(numeros)
   # selectionSort(numeros)
   # print(numeros)

    shuffle(numeros)
    print(numeros)
    insertionSort(numeros)
    print(numeros)
