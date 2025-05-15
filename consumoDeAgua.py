peso = float(input("Introduce tu peso en kg: "))
actividad = input("Introduce tu nivel de actividad (bajo, medio o alto): ").lower()
consumo = float(input("¿Cuánta agua has consumido hoy en ml? "))

def calcular_objetivo_ml(peso_kg, nivel_actividad):

    objetivo_base = peso_kg * 35


    if nivel_actividad == "bajo":
        objetivo_ml = objetivo_base * 0.90 

    elif nivel_actividad == "alto":
        objetivo_ml = objetivo_base * 1.10

    else:
        objetivo_ml = objetivo_base  

    return (objetivo_ml)

objetivo = calcular_objetivo_ml(peso, actividad)

def estado_hidratacion(consumo_ml, objetivo_ml):
    porcentaje = (consumo_ml / objetivo_ml) * 100
    if porcentaje >= 100:
        return f"Has alcanzado tu objetivo"
    elif porcentaje < 100:
        diferencia = objetivo_ml - consumo_ml
        return f"Te falta un {diferencia} ml para llegar"
    else:
        diferencia = consumo_ml - objetivo_ml
        return f"Has excedido tu objetivo en {diferencia} ml"
estad_hidratación_final = estado_hidratacion(consumo, objetivo)

print(f"\nObjetivo diario de agua: {objetivo} ml")
print(estad_hidratación_final)
