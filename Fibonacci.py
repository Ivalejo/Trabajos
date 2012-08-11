#-------------------------------------------------------------------------------
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()
    n = int(input('Digite cantidad de numeros para la serie Fibonacci'))

print('Secuencia Fibonacci:')

a = 0
b = 1

i = 0
while i < n:

    print a
    print b
    a = a + b
    b = a + b
    i = i + 1
