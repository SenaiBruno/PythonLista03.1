"""
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
"""

dist = int(input("Qual a distancia da sua viagem ( em Km/h ):"))

cons = int(input("Qual é o consumo médio de gasolina do automovel ( em Km/h )"))

litros = dist / cons

print("Você gastara:", litros,"litros de gasolina")
