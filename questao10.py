"""
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
"""

valor=float(input("Qual o valor a ser pago?:"))

taxa=float(input("Qual é a taxa?:"))

dias=float(input("Qual o tempo (em dias)"))

formula = valor + (valor * (taxa / 100) * dias)

print("Sua prestação em atraso é de R$:", formula)