import csv

def lee_variaciones_temperatura(fichero):
    lista=[]
    with open(fichero,encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)
        for i,registro in enumerate(lector):
            lista.append(tuple(registro))
            if i==4:
                break
    return lista 

if __name__=="__main__":
    lista_total=lee_variaciones_temperatura("data/monthly_csv.csv")
    print(lista_total)