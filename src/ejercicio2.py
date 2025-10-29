def extrae_numeros(texto):
    lista=[]
    numero=""
    for i in texto:
        if i.isdigit():
            numero+=i
        else:
            if numero!="":
                lista.append(int(numero))
                numero=""
    return lista

if __name__=="__main__":
    numeros=extrae_numeros("Este año la empresa ganó 12432 euros de 8 contratos")
    print(numeros)

#Defina una función `extrae_numeros` que reciba un texto y devuelva todas aquellas cantidades que aparezcan dentro del texto. 
#Por ejemplo, si el texto es "Este año la empresa ganó 12432 euros de 8 contratos", la función devuelve `[12432, 8]`. 
#Observe que los elementos de la lista devuelta son de tipo `int