#Função 1 (normalizando bases de países)

def normaliza(dicionario):     
    dic_novo = {}

    for continente, paises in dicionario.items():
        for pais, dados in paises.items():
            dados['continente'] = continente
            dic_novo[pais] = dados

    return dic_novo 

#Função 2 (sorteando países)

import random 

def sorteia_pais(lista):
    saida = list(lista.keys())
    return random.choice(saida)
    
#Função 3 (Distancia de Haversine)    

import math
from math import pi

def haversine(raio,p1,l1,p2,l2):
    p1raio = p1 * (pi/180)
    l1raio = l1 * (pi/180)
    p2raio = p2 * (pi/180)
    l2raio = l2 * (pi/180)
    diferenca1 = float(p2raio - p1raio)
    diferenca2 = (l2raio - l1raio)
    vv1 = math.sin(diferenca1/2)**2
    vv2 = math.cos(p1raio)
    vv3 = math.cos(p2raio)
    vv4 = math.sin(diferenca2/2)**2
    vv5 = vv1 + vv2 * vv3 * vv4
    vv6 = vv5**(1/2)
    d = 2*raio*math.asin(vv6)
    d_final = d
    
    return d_final
    
    
#Função 4 (adicionando em uma lista ordenada)

def adiciona_em_ordem(nome, dist, lista):
    cont = 0
    for k in range(0, len(lista)):
        if lista[k][1] < dist:
            cont +=1
    lista.insert(cont, [nome,dist])
    return lista
    
#Função 5 (Esta na lista?)

def esta_na_lista(nome, lista):
    cont = 0
    for k in range(len(lista)):
        if nome in lista[k]:
            cont += 1
    if cont == 0:
        return False
    else:
        return True


#Função 6 (Sorteia letra com restrições)


import random

def sorteia_letra(palavra, letra):
    lista = []
    restr = ['.', ',', '-', ';', ' ']
    for k in range(len(palavra)):
        if palavra[k] not in restr and palavra[k] not in letra:
            lista.append(palavra[k])

        return random.choice(lista)






