
def main():
    #escribe tu código abajo de esta línea
def papel(p,u):
    a = p*12
    return a
def plumones(p,u):
    b = u*35
    return b
def main():
    p = int(input("Dame la cantidad de pliegos de papel albanene:"))
    u = int(input("Dame la cantidad de plumones:"))
    if p<u:
        m = papel(p,u)
        print("El número máximo de tarjetas que se pueden hacer es:")
        print(m)
    elif p+1>u:
        j = plumones(p,u)
        print("El número máximo de tarjetas que se pueden hacer es:")
        print(j)

if __name__=='__main__':
    main()
