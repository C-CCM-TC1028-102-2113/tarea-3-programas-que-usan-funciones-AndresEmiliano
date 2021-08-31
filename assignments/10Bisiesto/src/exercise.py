
def main():
    #escribe tu código abajo de esta línea
def bisiesto(h):
    if h%4==0:
        if h%100 !=0 or h%400==0:
            print("true")
        else:
            print("false")
    else:
        print("false")

def main():
    h = int(input("dame el año:"))
    a = bisiesto(h)

main()

if __name__=='__main__':
    main()
