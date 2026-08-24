import matplotlib.pyplot as plt

consumo = {"segunda":18, "terca":22, "quarta":20, "quinta":25, "sexta":30, "sabado":12, "domingo":10}

plt.bar(consumo.keys(), consumo.values(), color='mediumpurple', edgecolor='black')

# Títulos e rótulos
plt.title('Consumo por dia da semana ')
plt.xlabel('Dias')
plt.ylabel('Consumo em kWh')

# Exibir o gráfico
plt.show()