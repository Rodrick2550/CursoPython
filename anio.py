def calculo():
    anio = int(input("Ingresa el año a calcular"))
    if(anio % 4 !=0):
        print('tu anio no es bisiesto')

    else:
        print('tu anio es bisiesto')

calculo()