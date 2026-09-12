"""
Métodos del grafo:
Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str

"""

import random

class Grafo:
    def __init__(self, es_dirigido = False, vertices_init = None):
        self.es_dirigido = es_dirigido
        self.vertices = {}
        if vertices_init is not None:
            for v in vertices_init:
                self.agregar_vertice(v)
        
    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}
    
    def borrar_vertice(self, v):
        if v not in self.vertices:
            raise ValueError("No se puede borrar un vertice que no existe")
        if not self.es_dirigido:
            while self.vertices[v]:
                w, _ = self.vertices[v].popitem()
                self.vertices[w].pop(v)
        else:
            for adyacencias in self.vertices.values():
                adyacencias.pop(v, None)
        self.vertices.pop(v)
            
    def agregar_arista(self, v, w, peso = 1):
        if v not in self.vertices:
            raise ValueError(f"El vértice '{v}' no existe en el grafo")
        if w not in self.vertices:
            raise ValueError(f"El vértice '{w}' no existe en el grafo")
        
        if not self.es_dirigido:
            self.vertices[w][v] = peso
        self.vertices[v][w] = peso
    
    def borrar_arista(self, v, w):
        if v not in self.vertices:
            raise ValueError(f"El vértice '{v}' no existe en el grafo")
        if w not in self.vertices:
            raise ValueError(f"El vértice '{w}' no existe en el grafo")
        
        if not self.es_dirigido:
            self.vertices[w].pop(v)
        self.vertices[v].pop(w) 
        
    def estan_unidos(self, v, w):
        if v not in self.vertices:
            raise ValueError(f"El vértice '{v}' no existe en el grafo")
        if w not in self.vertices:
            raise ValueError(f"El vértice '{w}' no existe en el grafo")
        return w in self.vertices[v]
        
    def peso_arista(self, v, w):
        if v not in self.vertices:
            raise ValueError(f"El vértice '{v}' no existe en el grafo")
        if w not in self.vertices:
            raise ValueError(f"El vértice '{w}' no existe en el grafo")
        if w not in self.vertices[v]:
            raise ValueError(f"No existe una arista entre '{v}' y '{w}'")
        return self.vertices[v][w]
    
    def obtener_vertices(self):
        return list(self.vertices.keys())
    
    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices())
    
    def adyacentes(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice '{v}' no existe en el grafo")
        return list(self.vertices[v].keys())
    