# ==============================================================================
# FATEC FERRAZ DE VASCONCELOS 
# Matéria: Estatística
# Professor: LUIZ CARLOS DOS SANTOS FILHO
# Programadores:
#               AUDREY BERGAMINE GALVÃO
#               VAGNER DA SILVA MATIAS   
#  
# Programa: CRUD Voltado para as cotações de ações
#Entrada: criação dados e arquivos txt
#Saída: Tabelas com os resultados dos cálculos

# ================================ IMPORTS =====================================
import Funcoes
import curses
import pandas
import os
from classMTC import *
from Crud import Crud

Lista_CRUDs = ["Create (Criar)", "Read (Ler)", "Update (Atualizar)", "Delete (Apagar)", "Calculate (Calcular)", "Exit (Sair)"] #Lista do menu.
#Instânciação da classe Crud
teste = Crud()


#Criação do loop com um menu de escolhas do uusário.
while True:
    teste.criarMenu(Lista_CRUDs,"Selecione abaixo as opções desejadas e pressione enter para confirmar:\n\n")
    if teste.nomeEscolhido =="Create (Criar)":                                      
        while True:
            if teste.criarBanco() == False:
                break        
    elif teste.nomeEscolhido =="Update (Atualizar)":
        teste.atualizarDados()
        #teste.Substituir()

    elif teste.nomeEscolhido =="Read (Ler)":
        teste.lerArquivos()

    elif teste.nomeEscolhido =="Delete (Apagar)":
        teste.deletarArquivos()

    elif teste.nomeEscolhido == "Calculate (Calcular)":        
        teste.calcular()
        

    elif teste.nomeEscolhido ==  "Exit (Sair)":
        print(color(f'\n>>> Muito obrigado por usar o ','azul',negrito=True) + color('ESTATIC','verde',negrito=True) + color('!!!','azul',negrito=True))
        break
