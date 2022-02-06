## desafio: crie um programa que receba uma entrada -> input (sempre minúsculo)
# A entrada terá dois nomes -> nome e sobrenome
# imprima: "As iniciais em maiúsculo são: "

#dica: .split()
'''
nome = input ("Digite o primeiro e ultimo nome: ")
x = nome.split()
y = x[0]
z = x[1]
print(y[0].upper())
print(z[0].upper())
print(x[0].upper(), #nome
      x.split()[1][0].upper() ) #sobrenome
Atividade 5 - Crie um programa que pergunte o nome do usuário e sua idade e imprima em cada linha:

Olá [nome do usuário].
Você tem [tantos] anos de idade.
Ano que vem você terá [tantos].
Daqui 5 anos você terá [tantos].

import random as rd

valor_escolhido = int(input('Entre com um valor de 1 a 10: '))
valor_aleatorio = rd.randint(1,10)

print(f'\nValor escolhido: {valor_escolhido}\nValor aleatório: {valor_aleatorio}')

valor_escolhido == valor_aleatorio



nome = input("Digite seu nome: ")
id = int(input("Digite sua idade atual "))
print(f"Olá {nome} \n Você tem {id} anos \n Ano que vem você terá : {id+1} \n E daqui a 5 anos {id+5} ")

'''