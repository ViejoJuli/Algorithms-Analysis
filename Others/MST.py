#MST-Minimun Spanning Tree-Arbol de Mínima Expansión
#Creación del grafo 
class Grafo: 

    def __init__(self, vertices):
        self.V = vertices #Crea vertices 
        self.grafo = []  #Lista de ejes del grafo
         
    #Funcion para agregar eje al grafo (v1,v2,peso), revisando que el número del vertice
    #No supere el número de vertices por parametro o sean vertices con valores negativos
    def agregarEje(self, u, v, w):
        if u>self.V-1 or v>self.V-1 or u<0 or v<0:
            print("El indice del vertice supera el número de vertices creados")
            return
        if u==v:
            print("Los vertices son iguales")
            return
        self.grafo.append([u, v, w])
 
    #Función find usando compresión
    def find(self, padre, i):
        if padre[i] == i:
            return i
        return self.find(padre, padre[i])
 
    #Función union de dos "arboles"
    def union(self, padre, nivel, x, y):
        xorg = self.find(padre, x) #Busca el origen de x
        yorg = self.find(padre, y) #Busca el origen de y
 
        #Asigna el arból con menor nivel en el de mayor nivel
        if nivel[xorg] < nivel[yorg]:
            padre[xorg] = yorg
        elif nivel[xorg] > nivel[yorg]:
            padre[yorg] = xorg
 
        #Si son iguales, se asigna uno al otro, y se aumenta el nivel del arbol en +1
        else:
            padre[yorg] = xorg
            nivel[x] += 1
 
    #Algorítomo de Kruskal
    def KruskalMST(self):
 
        respuesta = []
         
        #Variable auxiliar para los verticies visitados
        i = 0
         
        #Variables auxiliar para llevar el número de vertices agregados al arbol de mínima expansión
        e = 0
 
        #Se organiza la lista de ejes por su peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2]) 
 
        #Lista de los padres de cada nodo
        padre = []
        
        #Lista de los niveles de cada nodo
        nivel = []
 
        #Se crean subsets individuales
        for vertice in range(self.V):
            padre.append(vertice)
            nivel.append(0)
 
        #Cuando el número de ejes dentro del arbol es igual al numero de vertices-1 
        #se detiene el algoritmo
        while e < self.V - 1:
            #Revisa que no se hayan visitado ya todos los nodos
            if i==len(self.grafo):
                print("No se puede realizar un MST porque el gráfo no es conexo")
                return
            #Se escoge el eje de menor valor
            u, v, w = self.grafo[i]
            i = i + 1 #aumenta el indice de la iter
            
            x = self.find(padre, u)
            y = self.find(padre, v)
             
            #Si al incluirse no se forma un ciclo, se incluye dentro de la respuesta y se hace union
            #Si no se descarta (no se hace nada con él)
            if x != y:
                e = e + 1 
                respuesta.append([u, v, w])
                self.union(padre, nivel, x, y)
 
        costo = 0
        print ("Ejes para el arbol de Mínima Expansión")
        for u, v, w in respuesta:
            costo += w
            print("%d -- %d == %d" % (u, v, w))
        print("Costo MST" , costo)
 
#Caso de Prueba
ejemplo = Grafo(4)
ejemplo.agregarEje(0, 1, 15)
ejemplo.agregarEje(0, 2, 26)
ejemplo.agregarEje(0, 3, 15)
ejemplo.agregarEje(1, 3, 10)
ejemplo.agregarEje(2, 3, 3)

#Caso de Pruebas Error
#ejemplo1 = Grafo(6)
#ejemplo1.agregarEje(0, 1, 15)
#ejemplo1.agregarEje(0, 2, 26)
#ejemplo1.agregarEje(0, 3, 15)
#ejemplo1.agregarEje(1, 3, 10)
#ejemplo1.agregarEje(2, 3, 3)
#ejemplo1.agregarEje(4, 5, 10)

#Función, se llama al metodo de la clase Grafo que corre Kruskal
ejemplo.KruskalMST()

#Función que bota error, se llama al metodo de la clase Grafo que corre Kruskal
#ejemplo1.KruskalMST()