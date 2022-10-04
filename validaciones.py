import re 
def validar_entero(numero_str:str)->int:
    result = re.match("^[0-9]+$",numero_str)
    if(result != None):
        return int(numero_str)
    else:
        return False

