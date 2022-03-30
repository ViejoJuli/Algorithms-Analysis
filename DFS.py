# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:06:01 2022

"""

import time

#Representación de grafo: Lista de Adyacencias, no dirigido, arreglo

'''
dfs_me 
Función recursiva que al encontrar en sí mismo el nodo raíz que se está buscando 
retorna True, de lo contrario retorna la operación lógica or entre la respuesta
de dfs_me de los nodos alcanzables no visitados desde node, y un false.

root: nodo raíz buscado
node: nodo actual
graph: lista de adyacencia
visited: arreglo de nodos visitados
'''
def dfs_me(root,node,graph,visited):
    ans = False
    if not visited[node]:
        visited[node] = 1
        for i in graph[node]:
            ans = ans or dfs_me(root,i,graph,visited)
    if root == node:
        return True
    return ans


'''
true_dfs 
Función que ejecuta la búsqueda DFS desde un nodo base, inicializa una lista de
nodos visitados y llama la función recursiva dfs_me desde los nodos alcanzables 
por este nodo raíz. Retorna True si encontró un autopréstamo, False de lo contrario

root: nodo actual
graph: lista de adyacencia
'''
def true_dfs (root, graph):
    visited = [0]*len(graph)   
    ans = False
    for i in graph[root]:
        ans = ans or dfs_me(root,i,graph,visited)        
    return ans

'''
look_cicles 
Función que llama a la función true_me desde todos los nodos, retorna True al
encontrar un autopréstamo, False de lo contrario.

graph: lista de adyacencia
'''
def look_cicles(graph):
    for i in range(len(graph)):
        if true_dfs(i,graph):
            return True
    return False


a1= look_cicles([[2,1],[3,4],[5],[],[5],[]])
a2= look_cicles([[2,1],[3,4],[5],[],[5],[0]])
a3= look_cicles([[1],[2],[0]])
a4= look_cicles([[1],[2],[]])
print("Expected False, received",a1)
print("Expected True, received",a2)
print("Expected True, received",a3)
print("Expected False, received",a4)

