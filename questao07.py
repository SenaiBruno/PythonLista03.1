"""
Fazer um algoritmo que pergunte 3 números e apresente a média aritmética entre estes 3 números.
"""

print("Escolha 3 números para saber a média aritmética entre estes 3 números")

num1 = int(input("Seu primeiro número:"))
num2 = int(input("Seu segundo número:"))
num3 = int(input("Seu terceiro número:"))

soma = (num1 + num2 + num3) /3

print ("Sua média: ",soma)