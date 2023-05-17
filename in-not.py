# Operadores in e not in 
# Strings em py são iteraveis 
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1  

# nome = 'Gabriel'
# print(nome[2])
# print('a' in nome)
# print('t' in nome)
# print(10 * '_')
# print('a' not in nome)

nome = input('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')   