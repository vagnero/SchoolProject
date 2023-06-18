#-- Funções de tratamento de texto

# Dicionário com as chaves em português como referência dos códigos de cores do terminal python.
coresTexto = { #Cores de texto

'':'',
'vermelho' : '\033[31m',
'verde' : '\033[32m',
'azul' : '\033[34m',
'roxo' : '\033[35m',

'ciano' : '\033[36m',
'magenta' : '\033[35m',
'amarelo' : '\033[33m',
'preto' : '\033[30m',

'branco' : '\033[37m',

'original' : '\033[0;0m',
'negrito' : '\033[1m',
'reverso' : '\033[2m',
}

coresFundo = { #Cores de fundo
'':'',
'preto' : '\033[40m',
'vermelho' : '\033[41m',
'verde' : '\033[42m',
'amarelo' : '\033[43m',
'azul' : '\033[44m',
'magenta' : '\033[45m',
'ciano' : '\033[46m',
'branco' : '\033[47m',
}

def color(texto,corT="",corF="",negrito=False):
#Função que recebe um texto, a cor do texto, a cor de fundo e se o usuário quer em negrito ou não.
#Por padrão, o negrito vem desativado
#Se o usuário não quiser alteração de um dos itens ele deixa uma string vazia, exemplo: color('texto','','vermelho') ou no caso do negrito, não apresenta ele no argumento.

    if negrito == True: # se o negrito for verdadeiro, ele edita seu valor para 'negrito' - chave referencia da opção do dicionário coresTexto
        negrito = 'negrito'
    else:
        negrito = '' # se o negrito for vazio, ele edita seu valor para '' - chave referencia da opção do dicionário coresTexto para '' também

    # Aqui ele junta tudo em uma String da forma que o Python entende a codificação de cores e retorna para o usuário essa string.
    return coresTexto[corT]+ coresFundo[corF] + coresTexto[negrito] + texto + coresTexto['original'] 



# print(f"{color('hello')} {color('world','azul')}")    