#(1) COMANDOS PARA O SISTEMA:
# -*- coding: utf-8 -*-
#(2) COMENTARIO GERAL
"""
SIMPAR – Simulação de Passageiros em Partida Aérea
"""
__author__= 'Inácio Galrito-30000016@students.ual.pt''\n''Ricardo Marques-30000386@students.ual.pt ''\n''Cátia Xavier-30000115@students.ual.pt''\n''Rute Martins-30000411@students.ual.pt '
__version__='V 1.0'
"""
"""
#(3) IMPORTAÇÃO DE MÓDULOS:
#import AED18PLA1_PyF1_CXavierJGalritoRMarquesRMartins
#help(AED18PLA1_PyF1_CXavierJGalritoRMarquesRMartins)
from pythonds.basic import Queue
import random
import copy
#(4) DECLARAÇÃO DE VARIÁVEIS:
num_pass = 70
num_bag = 4
num_balcoes = 4
ciclos = 10
ciclo_atual = 0
balcoes = []
#(5) DECLARAÇÃO DE CLASSES:
class Passageiro:
    def __init__(self, bag_pass, ciclo_in):
        self.bag_pass = bag_pass
        self.ciclo_in = ciclo_in
    def __str__(self):
        return ("[b:{} t:{}]" .format(self.bag_pass, self.ciclo_in))
#        devolve uma string com formatação dos atributos, conforme o
#  		      exemplo de um passageiro com 4 bagagens no ciclo da simulação 2: [b:4 t:2]    
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
        self.bag_utemp = bag_utemp
    def __str__(self):
#        Apresenta em lista os atributos e respetivos valores do balcão
        return "Balcão Nº: " + str(self.n_balcao) + \
    "\n" + "Tamanho da fila de espera: " + str(self.obtem_tam_fila()) + \
    "\n" + "Fila de espera: " + str(self.obtem_pass_fila()) + \
    "\n" + "inic_atend: " + str(self.inic_atend) + \
    "\n" + "passt_atend: " + str(self.passt_atend) + \
    "\n" + "numt_bag: " + str(self.numt_bag) + \
    "\n" + "tempt_esp: " + str(self.tempt_esp) + \
    "\n" + "bag_utemp: " + str(self.bag_utemp)

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
    return Passageiro(random.randint(1,num_bag), copy.deepcopy(ciclo_atual))
#função principal
def simpar_simula():
    cria_balcoes()
    

    

            
#(7) CORPO PRINCIPAL DO PROGRAMA:
if __name__ == '__main__':
    simpar_simula()
    balcoes[0].fila.enqueue(1)
    balcoes[0].fila.enqueue(1)
    balcoes[0].fila.enqueue(1)
    balcoes[1].fila.enqueue(1)
    balcoes[1].fila.enqueue(1)
    balcoes[1].fila.enqueue(1)
    balcoes[2].fila.enqueue(1)
    balcoes[2].fila.enqueue(1)
    balcoes[3].fila.enqueue(1)
    for b in range(len(balcoes)):
        print(balcoes[b])
        
    print(escolhe_filaMaisCurta())
    print(gera_passageiro())
    
#   PARA APAGAR - só para verificar que foram criados os balcoes - PARA APAGAR
#    for b in range(len(balcoes)):
#        print (balcoes[b])
#   PARA APAGAR - só para verificar que foram criados os balcoes - PARA APAGAR
