from time import *
from datetime import *


def calcula_edad(fecha):
    hoy = date.today()

    edad = hoy.year - fecha.year
    if (hoy.month, hoy.day) < (fecha.month, fecha.day):
        edad -= 1
    
    proximo_cumple = date(hoy.year, fecha.month, fecha.day)


    if proximo_cumple < hoy:
            proximo_cumple = date(hoy.year + 1, fecha.month, fecha.day)

    dias_faltan = (proximo_cumple - hoy).days
    return edad, dias_faltan
if __name__=="__main__":
    fecha_nacimiento=date(2008,10,8)
    edad,dias=calcula_edad(fecha_nacimiento)
    print(f"Tienes {edad} años. Quedan {dias} días para tu cumpleaños")