def es_bisiesto(año):
    if año%400==0 or (año%4==0 and not año%100==0):
        return True
    else:
        return "el año no es bisiesto"
    
if __name__=="__main__":
    año_bisiesto=es_bisiesto(2025)
    print(año_bisiesto)

#Pruebe la función anterior pasándole los años 2000, 2024, 1900 y 2025 (los dos primeros son bisiestos, los dos últimos no).