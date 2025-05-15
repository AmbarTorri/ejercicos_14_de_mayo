print ("Maquina calculadora de dias del promedio")

total_gastado = int(input("ingrese el total que gasto en su viaje"))
numero_dias = int(input("ingrese el numero de dias que estuvo en su viaje"))

def calcular_gasto_promedio(total_gastado, numero_dias):
    Gasto_Promedio = total_gastado / numero_dias
    return Gasto_Promedio
Gasto_Promedio_Diario= calcular_gasto_promedio(total_gastado, numero_dias)
print (Gasto_Promedio_Diario)

presupuesto = int(input("ingrese el presupuesto inicial"))

def calcular_balance(presupuesto, Gasto_Promedio_Diario):
    Dinero_restante = presupuesto - Gasto_Promedio_Diario
    if  presupuesto < Gasto_Promedio_Diario:
        print("no es posible gastar mas dinero del que llevo")
    else:
        return Dinero_restante
Dinero_que_queda = calcular_balance(presupuesto, Gasto_Promedio_Diario)
print (Dinero_que_queda)
    
