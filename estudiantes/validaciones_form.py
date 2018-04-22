

def validador_solo_letras(value):
    if str(value).isalpha():
        return True
    else:
        return False


def validador_solo_espacios_vacios(value):
    if str(value).isspace():
        return False
    else:
        return True