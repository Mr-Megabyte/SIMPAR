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
ciclos = 1
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
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self != None:
            postorder(self.getLeftChild())
            postorder(self.getRightChild())
            print(self.getRootVal())
        
    def inorder(self):
        if self != None:
            inorder(self.getLeftChild())
            print(self.getRootVal())
            inorder(self.getRightChild())
      
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
    
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
    
def passTree():
    i=0
    for i in range(0, 69):
        names.get_full_name()
        print ("\n" ,names.get_full_name())
        i = i + 1
         
            
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
#    print(escolhe_filaMaisCurta())
#atende_passageiros()
#    print("A probabilidade de chegar mais um passageiro é " + str(chega_passageiro()) + "%")

mytree = BinarySearchTree()
mytree[17]= names.get_full_name()
mytree[24]= names.get_full_name()

print("\n" + mytree[17])
print(mytree[24])
