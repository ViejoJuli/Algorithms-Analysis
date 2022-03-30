#Maximun Bipartite Matching utilizando el algoritmo de Edmond Karp.
from collections import defaultdict
class MBM:
    def __init__(self,M,N):
        self.personas=M
        self.trabajos=N
        self.grafo=defaultdict(list) #Diccionario que guardo los vertices

    def agregarEjes(self,conexiones):
        for conexion in conexiones:
            print(conexion[0],conexion[1])
            self.grafo[conexion[0]].append(conexion[1])
            print(self.grafo)
    
    def bfs(self,u,matchR, seen): #Por defecto inicia en el trabajador 0
        for v in range(self.jobs):
            if 
    """
    def bfs(self, u, matchR, seen):
        # Try every job one by one
        for v in range(self.jobs):
 
            # If applicant u is interested
            # in job v and v is not seen
            if self.grafo[u][v] and seen[v] == False:
                 
                # Mark v as visited
                seen[v] = True
 
                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False
    def maxBPM(self):
        '''Array de -1 de trabajos asignados, si el número
        cambia es igual a la persona a la que fue asignada'''
        matchR = [-1] * self.trabajos 
        #Recorrido por cada una de las personas
        for i in range(self.ppl): 
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
            # Find if the applicant 'u' can get a job
            if self.bfs(i, matchR, seen):
                result += 1
        return result
    """
ejemplo = MBM(6,6)
ejemplo.agregarEjes([[5,5],[0,4],[1,4],[1,2],[1,1],[2,4],[2,2],[2,0],[2,1],[2,3],[3,4]])
