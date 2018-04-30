#(1) COMANDOS PARA O SISTEMA:
# -*- coding: utf-8 -*-
#(2) COMENTARIO GERAL
"""
Created on Mon Apr 30 01:41:13 2018

SIMPAR – Simulação de Passageiros em Partida Aérea
"""
__author__= 'Inácio Galrito-30000016@students.ual.pt''\n''Ricardo Marques-30000386@students.ual.pt ''\n''Cátia Xavier-30000115@students.ual.pt''\n''Rute Martins-30000411@students.ual.pt '
__version__='V 1.0'
"""
"""
#(3) IMPORTAÇÃO DE MÓDULOS:
import SIMPAR
help(SIMPAR)
#(4) DECLARAÇÃO DE VARIÁVEIS:
#(5) DECLARAÇÃO DE CLASSES:
class Passageiro:
    def __init__(self, bag_pass, ciclo_in):
        self.bag_pass = bag_pass
        self.ciclo_in = ciclo_in
#    def __str__(self):
#        devolve uma string com formatação dos atributos, conforme o
#  		      exemplo de um passageiro com 4 bagagens no ciclo da simulação 2: [b:4 t:2]
# def obtem_bag_pass(self):
#        devolve o valor de bag_pass
# def obtem_ciclo_in(self):
#        devolve o valor de ciclo_in
class Balcao:
    def __init__(self,n_balcao,fila,inic_atend,passt_atend,numt_bag,tempt_esp,bag_utemp):
        self.n_balcao = n_balcao
        self.fila = fila
        self.inic_atend = inic_atend
        self.passt_atend = passt_atend
        self.numt_bag = numt_bag
        self.tempt_esp = tempt_esp
        self.bag_utemp = bag_utemp
#    def __str__(self):
#    def muda_inic_atend():
#    def incr_passt_atend():
#    def muda_numt_bag():
#    def muda_tempt_esp():
    def obtem_fila(self):
        return self.fila
        
#(6) DECLARAÇÃO DE FUNÇÕES:
#(7) CORPO PRINCIPAL DO PROGRAMA:
