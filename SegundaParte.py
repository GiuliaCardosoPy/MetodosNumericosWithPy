import matplotlib.pyplot as plt

consumo = {"segunda":18, "terca":22, "quarta":20, "quinta":25, "sexta":30, "sabado":12, "domingo":10}

valores = list(consumo.values())

maior = max(valores)
menor = min(valores)

colors = []

for valor in valores:
    if valor == maior:
        colors.append('red')  
    elif valor == menor:
        colors.append('green') 
    else:
        colors.append('orange') 

plt.bar(consumo.keys(), valores, color=colors, edgecolor='black')

plt.title('Consumo por dia da semana ')
plt.xlabel('Dias')
plt.ylabel('Consumo em kWh')

plt.savefig("grafico.png")

plt.show()
