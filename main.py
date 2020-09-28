dia = int(input("Dia: "))
mes = int(input("Mes: "))

if (mes == 12 and (dia >= 22 and dia <= 31)) or (mes == 1 and (dia <= 20 and dia >= 1)):
    print("capricornio")
elif(mes == 1 and (dia > 20 and dia <= 31)) or (mes == 2 and (dia <= 19 and dia >= 1)):
    print("acuario")
elif(mes == 2 and (dia > 19 and dia <= 28)) or (mes == 3 and (dia <= 20 and dia >= 1)):
    print("piscis")
elif(mes == 3 and (dia > 20 and dia <= 31)) or (mes == 4 and (dia <= 20 and dia >= 1)):
    print("aries")
elif(mes == 4 and (dia > 20 and dia <= 30)) or (mes == 5 and (dia <= 21 and dia >= 1)):
    print("tauro")
elif(mes == 5 and (dia > 21 and dia <= 31)) or (mes == 6 and (dia <= 21 and dia >= 1)):
    print("geminis")
elif(mes == 6 and (dia > 21 and dia <= 30)) or (mes == 7 and (dia <= 23 and dia >= 1)):
    print("cancer")
elif(mes == 7 and (dia > 23 and dia <= 31)) or (mes == 8 and (dia <= 23 and dia >= 1)):
    print("leo")
elif(mes == 8 and (dia > 23 and dia <= 31)) or (mes == 9 and (dia <= 23 and dia >= 1)):
    print("virgo")
elif(mes == 9 and (dia > 23 and dia <= 30)) or (mes == 10 and (dia <= 23 and dia >= 1)):
    print("libra")
elif(mes == 10 and (dia > 23 and dia <= 31)) or (mes == 11 and (dia <= 22 and dia >= 1)):
    print("escorpio")
elif(mes == 11 and (dia > 22 and dia <= 30)) or (mes == 12 and (dia <= 21 and dia >= 1)):
    print("sagitario")
else:
    print("error")
