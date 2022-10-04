
def swap(lyst, i, j):
    """ Troca os itens nas posições i e j ."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:  # Faz n - 1 pesquisas
        minIndex = i  # pelo menor
        j = i + 1
        while j < len(lyst):  # Inicia uma pesquisa
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:  # Troca se necessário
            swap(lyst, minIndex, i)
        i += 1
