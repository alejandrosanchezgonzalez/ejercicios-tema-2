from time import *
from datetime import *

def calcula_edad(fecha):
    hoy=date.today()
    edad=hoy.year - fecha.year
    if (hoy.month, hoy.day)< (fecha.month, fecha.day):
        edad-=1
    cumpleaños= date(hoy.year,fecha.month, fecha.year)
    if cumpleaños<hoy:
        cumpleaños=date(hoy.year +1,fecha.month, fecha.day)
        faltan=(cumpleaños-hoy).days
    return edad,faltan

if __name__=="__main__":
    fecha_nacimiento=date(2008,10,8)
    edad,dias=calcula_edad(fecha_nacimiento)
    print(f"Tienes {edad} años. Quedan {dias} días para tu cumpleaños")