'''Si queremos hacerlo con
valores numéricos'''

edad = int(input("Cuántos años tienes?"))
def mayor_de_edad(edad):
    if(edad>=18):
        print("Así que eres mayor de edad...")
    else:
        print("Aún eres joven para ir a la disco por la noche")

mayor_de_edad(edad)