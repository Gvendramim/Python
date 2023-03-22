# lista = [1, 2, 3, 4 ,5] #Criação de uma lista
# lista [2] = 8 #troca um item na lista
# lista.append(7) #Adiciona um item na lista
# lista.sort(reverse=True) #deixa em sequencia
# lista.insert(2, 3) #Adiciona um item na lista na posição selecionada
# lista.pop() #Remove itens da Lista
# print(lista)

# from sys import _enablelegacywindowsfsencoding


Lista = list()
for cont in range(0, 5):
    Lista.append(int(input('Digite um valor:')))

for c, v in enumerate(Lista):
    print(f'na posição {c} encontrei o valor{v}!')
    print('Cheguei ao final da Lista.') #IMPORTANTE

    