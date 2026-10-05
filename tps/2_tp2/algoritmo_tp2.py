"""
tiene que ser una de doble variable, posible llenar matriz?

"""


"""
boceto ec. recurrencia hecha el miercoles (23)

OPT(i), siendo i la cantidad de monedas en el arreglo.

casos base:
OPT(0) = 0
OPT(1) = M[0]
OPT(2) = max(M[0], M[-1])
OPT(3) = max(M[0], M[-1]) + OPT(M-EleccionS-EleccionM)

OPT(n) = max(M[0] + OPT(M-M[0]-EleccionM), M[-1] + OPT(M-M[-1]-EleccionM))

eso fué lo planteado, despues seguí con boludeces de matrices y 


Esta mal igual.

bien para una primer idea. pero le falta.

tiene que ser manejo de dos variables. inicio y fin, para representar el "sacar" del arreglo M las elecciones elegidas. (consejo de Eze)


"""