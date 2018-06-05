# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:29:32 2018

@author: José Galrito
"""

#(1) COMANDOS PARA O SISTEMA:
# -*- coding: utf-8 -*-
#(2) COMENTARIO GERAL
"""
SIMPAR – Simulação de Passageiros em Partida Aérea
"""
__author__= 'Cátia Xavier-30000115@students.ual.pt''\n''Inácio Galrito-30000016@students.ual.pt''\n''Ricardo Marques-30000386@students.ual.pt ''\n''Filipe Ferreira-30000379@students.ual.pt''\n''Rute Martins-30000411@students.ual.pt '
__version__='V 1.0'
"""
"""
#(3) IMPORTAÇÃO DE MÓDULOS:
#import AED18PLA1_PyF1_CXavierJGalritoRMarquesRMartinsFFerreira
#help(AED18PLA1_PyF1_CXavierJGalritoRMarquesRMartinsFFerreira)
from pythonds.basic import Queue
import random
import copy
import names
#(4) DECLARAÇÃO DE VARIÁVEIS:
num_pass = 70
num_bag = 4
num_balcoes = 4
ciclos = 4
ciclo_atual = 0
balcoes = []
#(5) DECLARAÇÃO DE CLASSES:
class Passageiro:
#     bag_pass aleatório entre 1 e num_pass. ciclo_in é cópia profunda de ciclo_atual
#    (se assim não fosse, cada vez que incrementasse ciclo_atual, ciclo_in de todos os passageiros alterava)
    def __init__(self):
        self.bag_pass = random.randint(1,num_bag)
        self.ciclo_in = copy.deepcopy(ciclo_atual)
    def __repr__(self):
        return ("[b:{} t:{}]" .format(self.bag_pass, self.ciclo_in))        
    def obtem_bag_pass(self):
        return self.bag_pass
    def obtem_ciclo_in(self):
        return self.ciclo_in
class Balcao:
    def __init__(self,n_balcao,fila,inic_atend,passt_atend,numt_bag,tempt_esp,bag_utemp):
        self.n_balcao = n_balcao
        self.fila = Queue()
        self.inic_atend = inic_atend
        self.passt_atend = passt_atend
        self.numt_bag = numt_bag
        self.tempt_esp = tempt_esp
        self.bag_utemp = random.randint(1, num_bag)
        self.namesPass = names.get_full_name()
    def __str__(self):
#        Apresenta em lista os atributos e respetivos valores do balcão
        return "Balcão Nº: " + str(self.n_balcao) + \
    "\n" + "Tamanho da fila de espera: " + str(self.obtem_tam_fila()) + \
    "\n" + "Passageiros em fila: " + str(self.obtem_pass_fila()) + \
    "\n" + "inic_atend: " + str(self.inic_atend) + \
    "\n" + "passt_atend: " + str(self.passt_atend) + \
    "\n" + "numt_bag: " + str(self.numt_bag) + \
    "\n" + "tempt_esp: " + str(self.tempt_esp) + \
    "\n" + "bag_utemp: " + str(self.bag_utemp) + "\n"

    def muda_inic_atend():
        pass
    def incr_passt_atend():
        pass
    def muda_numt_bag():
        pass
    def muda_tempt_esp():
        pass
#    função para devolver os passageiros da fila
    def obtem_pass_fila(self):
        return self.fila.items
#    função para devolver o tamanho da fila
    def obtem_tam_fila(self):
        return self.fila.size()
    def obtem_balcao(self):
        return self.n_balcao
    def obtem_inic_atend(self):
        return self.inic_atend
    def obtem_passst_atend(self):
        return self.passt_atend
    def obtem_numt_bag(self):
        return self.numt_bag
    def obtem_tempt_esp(self):
        return self.tempt_esp
    def obtem_bag_utem(self):
        return self.bag_utemp
      
class node: #Declaração da classe Nó para ser usada na BST
    def __init__(self, value=None): #Inicia o valor dos NÓS como vazios
        self.value = value
        self.ladEsq = None #Nós a esq Vazios
        self.ladDrt = None #Nós a Drt vazios

class BinaryST:
    def __init__(self): #Arranca a Arvore com...
        self.root = None # a RAIZ vazia
    
    def insert(self, value): #Define o metodo insert
        if self.root == None: #Se o NO estiver vazio
            self.root = node(value) #Insere valor
        else:
            self._insert(value, self.root) #Caso nao insiramos o valor na raiz, 
                                            #invocamos a função privada _insert devido ao efeito recursivo
    def _insert(self, value, cur_node): #metodo privado para executar função recursiva
        if value < cur_node.value:
            if cur_node.ladEsq==None:
                cur_node.ladEsq=node(value)
            else:
                self._insert(value, cur_node.ladEsq)
        elif value > cur_node.value:
            if cur_node.ladDrt==None:
                cur_node.ladDrt=node(value)
            else:
                self._insert(value, cur_node.ladDrt)
        else:
            print ("Fim")
    
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, cur_node):
        if cur_node !=None:
            self._print_tree(cur_node.ladEsq)
            print (str(cur_node.value))
            self._print_tree(cur_node.ladDrt)
#(6) DECLARAÇÃO DE FUNÇÕES:
def cria_balcoes():
#    Encher a lista balcoes gerando objetos da classe Balcao até atingir num_balcoes
    while len(balcoes) < num_balcoes:
        balcoes.append(Balcao(len(balcoes)+1, 0, 0, 0, 0, 0, 0))
# função para escolher a fila mais pequena
def escolhe_filaMaisCurta():
# extraio o size da fila de cada balcão e construo um dicionario (filas) com {balcão(b):tamanho da fila(t)}.
    filas = {}
    for b in balcoes:
        filas.update({b.n_balcao:b.fila.size()})
# a seguir uso o sorted para ordenar os balcoes por size de fila mais pequeno para o maior e coloco numa lista de tuplos
    ordemCrescente = [(balcao, filas[balcao]) for balcao in sorted(filas, key=filas.get, reverse=True)]
# por último retorno o valor referente ao número do balcão do primeiro tuplo da lista que, por estar ordenada, será
# o que tem a fila mais curta 
    return(ordemCrescente.pop()[0])
# função que gera novos passageiros - bag_pass aleatório entre 1 e num_pass. ciclo_in é cópia profunda de ciclo_atual
#    (se assim não fosse, cada vez que incrementasse ciclo_atual, ciclo_in de todos os passageiros alterava)
def gera_passageiro():
    return Passageiro()
#    return Passageiro(random.randint(1,num_bag), copy.deepcopy(ciclo_atual))

# função para calcular a probabilidade de aparecer mais um passageiro mediante o ciclo_atual
def chega_passageiro():
#    divido ciclos por 3 para achar a terça parte do número total de ciclos
#    faço esta divisão recorrendo apenas à parte inteira do quociente, despresando o resto (//)
#    se a terça parte do número total de ciclos for maior ou igual ao ciclo atual, então
#    a probabilidade de chegar um novo passageiro é 100%
    if ciclos//3 >= ciclo_atual:
        return(100)
#    se duas vezes a terça parte do número total de ciclos for maior ou igual ao ciclo atual, então
#    a probabilidade de chegar um novo passageiro é 80%
    elif 2*ciclos//3 >= ciclo_atual and ciclo_atual > ciclos//3:
        return(80)
#   todos os outros resultados são para o terceiro terço do número de total de ciclos e a probabilidade é 60%
    else:
        return(60)
# função para atender passageiros
def atende_passageiros():
    for b in balcoes:
        if b.fila.isEmpty() == False:
            print(b.fila.dequeue())
            chega_passageiro()
            
#função principal
def simpar_simula():
    cria_balcoes()
          
#(7) CORPO PRINCIPAL DO PROGRAMA:
if __name__ == '__main__':
    #print(ciclo_atual)
    #print(ciclos)    
    while not ciclo_atual == ciclos:
        print("««« CICLO n.º {} »»»" .format(ciclo_atual + 1))
        ciclo_atual = ciclo_atual + 1
        simpar_simula()
            
        balcoes[0].fila.enqueue(Passageiro())
        balcoes[0].fila.enqueue(Passageiro())
        balcoes[0].fila.enqueue(Passageiro())
        balcoes[1].fila.enqueue(Passageiro())
        balcoes[1].fila.enqueue(Passageiro())
        balcoes[1].fila.enqueue(Passageiro())
        balcoes[2].fila.enqueue(Passageiro())
        balcoes[2].fila.enqueue(Passageiro())
        balcoes[3].fila.enqueue(Passageiro())
        for b in range(len(balcoes)):
            print("\n")
            print(balcoes[b])

                 
    print("O balcão com fila mais curta: ", escolhe_filaMaisCurta())
print("\nOs lugares de passageiros encontram-se preenchidos. \n"\
      "Eis a lista. \n")
mytree = BinaryST()
for i in range(0, 70):
    #mytree[i]= names.get_full_name()
    mytree.insert(names.get_full_name())
    
print (mytree.print_tree())
