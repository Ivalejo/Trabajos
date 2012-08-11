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

def insertionSort(a, ini, fin):
    for i in xrange(ini, fin + 1):
        # Insert a[i] into the sorted sublist
        v = a[i]
        for j in xrange(i-1, -1, -1):
            if a[j] <= v:
                a[j + 1] = v
                break
            a[j + 1] = a[j]
        else:
            a[0] = v
    return a

def PrintArray(array):
    for x in range(len(array)):
        sys.stdout.write(str(array[x]) + ",")
    sys.stdout.write("\n")

def main():
    t1=time.clock()
    print("Tiempo Inicio Ejecucion : ",t1)
    print ("Vector inicial")
    l=[3,5,7,9,3,1,2,0,6]
    PrintArray(l)
    r=insertionSort(l,0,8)
    PrintArray(r)
    print r
    t2=time.clock()
    print("Tiempo tomado Ordenamiento : ",(t2-t1))


if __name__ == '__main__':
    main()
