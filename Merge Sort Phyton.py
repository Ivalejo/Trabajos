#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      IvalejoSound
#
# Created:     08/10/2012
# Copyright:   (c) IvalejoSound 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()
import time
import sys
def merge_sort(m):
    if len(m) <= 1:
        return m

    medio = len(m) / 2
    izq = m[:medio]
    derecha = m[medio:]

    izq = merge_sort(izq)
    derecha = merge_sort(derecha)
    return list(merge(izq, derecha))



def merge(izq, derecha):
    resultado = []
    izq_idx, derecha_idx = 0, 0
    while izq_idx < len(izq) and derecha_idx < len(derecha):
        if izq[izq_idx] <= derecha[derecha_idx]:
            resultado.append(izq[izq_idx])
            izq_idx += 1
        else:
            resultado.append(derecha[derecha_idx])
            derecha_idx += 1

    if izq:
        resultado.extend(izq[izq_idx:])
    if derecha:
        resultado.extend(derecha[derecha_idx:])
    return resultado

def PrintArray(array):
    for x in range(len(array)):
        sys.stdout.write(str(array[x]) + ",")
    sys.stdout.write("\n")

def main():
    t1=time.clock()
    print("Tiempo Inicio Ejecucion : ",t1)
    print ("Vector inicial")
    l=[3,5,7,9,3,1,2,0,6,8,9,25]
    PrintArray(l)
    r=merge_sort(l)
    PrintArray(r)
    print r
    t2=time.clock()
    print("Tiempo tomado Ordenamiento : ",(t2-t1))


if __name__ == '__main__':
    main()