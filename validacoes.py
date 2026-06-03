def validar(escolha):
    if escolha.isnumeric() and 1 <= int(escolha) <= 5:
        return True
    else:
        return False 


def validar_indice(indice, total):
    if indice.isnumeric() and 1 <= int(indice) <= total:
        return True
    else:
        return False