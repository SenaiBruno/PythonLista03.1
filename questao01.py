"""
Desenvolver um programa que pergunte ao usuário o seu nome completo e seu sexo. Em seguida, o programa
deve apresentar os dados anteriormente informados.
"""

nome = input("Qual é o seu nome?")
print(type(nome))

sexo = input("Qual o seu sexo?")
print(type(sexo))

idade = input("Qual sua idade?")
print(type(idade))

print("Ola,", nome, "do sexo ", sexo, ", de", idade, "anos de idade")
