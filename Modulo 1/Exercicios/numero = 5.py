numero =int(input("digite o numero da tabuada:"))

inicio =int(input("digite o numero_inicio:"))

final =int(input("digite o numero_final:"))

for i in range (inicio,final+1):
    print (f"{numero} * {i} = {i*numero}")