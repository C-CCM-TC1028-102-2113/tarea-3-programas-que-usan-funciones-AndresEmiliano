
def main():
    #escribe tu código abajo de esta línea
def areaRect(b,h):
    a = b*h
    return a    
def main():
    b = float(input("dame la base:"))
    h = float(input("dame la altura:"))
    p = float(input("dame la profundidad:"))
    print("el volumen de un prisma es:")
    m=areaRect(b,h)*p
    print(m)
    

if __name__=='__main__':
    main()
