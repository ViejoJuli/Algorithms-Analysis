#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
import sys

from numpy import char

def build_array(text):
    sufix = []
    orig = {}
    for i in range(len(text)+1):
        sufix.append(text[i::]+'$')
        orig[text[i::]+'$']=i
    sufix.sort()
    finalsufix = []
    for i in sufix:
        finalsufix.append(orig[i])
    return finalsufix


def find(text,sufixarray,consult):
    pos = binary_search(text,sufixarray,consult)
    if pos == -1:return -1
    else:
        the_pos = []
        up = pos
        down = pos-1
        while up<len(sufixarray) and text[sufixarray[up]::].startswith(consult):
            the_pos.append(sufixarray[up])
            up+=1
        while down > -1 and text[sufixarray[down]::].startswith(consult):
            the_pos.append(sufixarray[down])
            down-=1
        return the_pos
    
def binary_search(text,sufixarray,consult):
    size = len(sufixarray)
    bot = 0
    top = size-1
    middle = 0
    while bot <= top:
        middle = (top+bot)//2
        piece = text[sufixarray[middle]::]
        if piece.startswith(consult):
            return middle
        elif piece > consult:
            top = middle -1
        elif piece < consult:
            bot = middle +1
    return -1

#Leer el archivo de entrada
with open (sys.argv[1]) as f:
    lines=f.readlines()
stringintro=''.join([str(item) for item in lines])
stringintro=stringintro.replace('\n','') #Elimina Enter
stringintro=stringintro.replace(' ','') #Elimina Espacios
print(build_array(stringintro))


'''
x = build_array("holabebeyaquecontigonosirvelalabia")
print(x)
y = build_array("biologia")
print(y)
z = build_array("banana")
print(binary_search("holabebeyaquecontigonosirvelalabia",x,"ia"))
print(find("banana",z,"na"))
q = build_array("nanananannanaaannananananannanananananana")
print(find("nanananannanaaannananananannanananananana",q,"na"))
'''
