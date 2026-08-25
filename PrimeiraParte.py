from colorama import Fore, init, Style



''' Desenvolva um programa em Python ou
 MATLAB que faça a Análise do consumo 
 de energia, situação problema:
 Uma escola deseja analisar o consumo de
 energia elétrica de uma sala de aula 
 durante 7 dias.
 Os consumos registrados foram:'''

init()

def separador():
    print("_________________________________________________________\n")
#1. Armazene os valores de consumo em um vetor/lista

consumo = {"segunda":18, "terca":22, "quarta":20, "quinta":25, "sexta":30, "sabado":12, "domingo":10}

#2. Calcule o consumo total da semana

consumo_total = 0
for dia in consumo:
    valor = consumo[dia]
    consumo_total += valor
    # print(consumo_total)

separador()  
print("2. Calcule o consumo total da semana") 
print (Fore.GREEN+ f"\nO consumo total da semana foi de \n{consumo_total} kWh" + Style.RESET_ALL)

#resposta: consumo total de 137kWh

#3. Calcule o consumo médio diário

for dia in consumo:
    media = consumo_total / len(consumo)

separador()
print("3. Calcule o consumo médio diário") 
print(Fore.GREEN + f"\nA média do consumo diário é {media} \nkWh por dia (valor aproximado {media:.2f})" + Style.RESET_ALL)

#resposta: consumo diário de 19.57kWH


#4. Identifique o maior consumo e em qual dia ocorreu


maior_consumo = max(consumo, key=consumo.get)

separador()
print("4. Identifique o maior consumo e em qual \ndia ocorreu") 
print(Fore.GREEN + f"\nO maior consumo foi {maior_consumo} \ncom {consumo[maior_consumo]} kWh" + Style.RESET_ALL)
#resposta: 30 kWh e sexta

#5. Identifique o menor consumo e em qual dia ocorreu
menor_consumo = min(consumo, key=consumo.get)


separador()
print("5. Identifique o menor consumo e em qual \ndia ocorreu") 
print(Fore.GREEN + f"\nO menor consumo foi {menor_consumo} \ncom {consumo[menor_consumo]} kWh" + Style.RESET_ALL)

#resposta: domingo com 10 kWh

#6.Determine quais dias tiveram consumo acima da média
dias_acima_media = []
nome_dias = []
for dia in consumo:
    valor = consumo[dia]
    if valor > media:
        dias_acima_media.append(valor)
        nome_dias.append(dia)

separador()
print("6.Determine quais dias tiveram consumo acima \nda média") 
print(f"\nA média foi de {media:.2f}")
print(Fore.GREEN + f"Os dias foram {nome_dias} \ne os valores {dias_acima_media}" + Style.RESET_ALL) 

#7. Calcule a porcentagem de redução do consumo no domingo em relação ao dia de maior consumo
consumo_domingo = consumo["domingo"]

erro_absoluto = consumo[maior_consumo] - consumo_domingo

erro_relativo = erro_absoluto / consumo[maior_consumo]

erro_percentual = erro_relativo * 100

arredondar_erro = round(erro_percentual, 2)

separador()
print("7. Calcule a porcentagem de redução do consumo no \ndomingo em relação ao dia de maior consumo" + Style.RESET_ALL)
print(Fore.GREEN + f"\nO percentual de redução foi de {erro_percentual}% \nou arredondando {arredondar_erro}%\n" + Style.RESET_ALL)

#resposta: 66.6666% ou 66.67%
