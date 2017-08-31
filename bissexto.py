
def is_bissexto(ano):
    if type(ano) is not int:
        raise TypeError("Ano deve ser inteiro.")
    if ano <= 0:
        raise ValueError("Ano deve ser maior do que zero.")

    if ano % 4 == 0 and ano % 100 != 0:
        return True

    if ano % 400 == 0:
        return True
        
    return False
