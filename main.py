from funcao import validador_idade

print('Seja bem-vindo ao site do Detran')

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

#Chamando a funcao corretamente
if validador_idade(idade):
    print(f'Acesso liberado {nome}')
else:
    print(f'Acesso negado {nome}! Espere mais alguns anos..')
