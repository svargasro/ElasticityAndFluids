import numpy as np
import matplotlib.pyplot as plt




#Se define la función.
def f(x):
    return np.cos(x) * np.cosh(x) - 1

ERRMAX=1e-7 #Se establece el error máximo.
#
def cerosPorBiseccion(a,b):
    fa=f(a)
    fb=f(b)
    if(fa*fb > 0):
        print("Los puntos a y b no son adecuados para encontrar la raíz.")
        return 1
    while (b-a)>ERRMAX:
        m = (a+b)/2.0
        fm = f(m)
        if (fm*fa<0):
            b=m
        else:
            a=m
            fa=fm

    return (a+b)/2

r1 = cerosPorBiseccion(3,7)
r2 = cerosPorBiseccion(5,10)
r3 = cerosPorBiseccion(9,14)

# print("La raíz 1 por método de bisección es x= ",r1)
# print("La raíz 2 por método de bisección es x= ",r2)
# print("La raíz 3 por método de bisección es x= ",r3)


# comment #####################################################################


def n(x,B,k,m):
    #valorAux = (np.sinh(m) - np.sin(m))/(np.cosh(m)-np.cos(m))

    #return B*(np.sinh(x) + np.sin(x) + valorAux*(np.cosh(x)+np.cos(x)))
    valorAux1 = (np.cosh(m)-np.cos(m))
    valorAux2 = (np.sinh(m)- np.sin(m))
   # print("Valor1: ", valorAux1)
   # print("Valo2: ", valorAux2)
    return B*(valorAux1*(np.sinh(k*x)+np.sin(k*x))- valorAux2*(np.cosh(k*x)+np.cos(k*x)))

#x = np.linspace(0,11,1000)

x=np.linspace(0,16,1600)


plt.style.use('seaborn-v0_8')

fig, axes = plt.subplots(figsize=(6, 7))



B1=1
k1=1
B2=1
k2=1
k3=1
B3=1

def orgFun1(k1,B1,r1,x):
    limD_X = 16.0
    limS_Y = 45.0
    limInf_Y = -115

    minVal = n(0,B1,k1,r1)
    print("El cero está en f1(x) = ", n(0,B1,k1,r1))
    maximo1 = np.max(n(x,B1,k1,r1))
    print("El máximo está en f1(x) = ", maximo1)

    valorIgualEn0 = 0
    for val in x:
        if np.abs(n(val,B1,k1,r1) - n(0,B1,k1,r1)) < 1  :
            valorIgualEn0 = val
    print("El valor de x donde f1(x) da igual a f(0) es : ", valorIgualEn0)

    k1= valorIgualEn0/limD_X
    B1 = limS_Y/maximo1

    minVal = n(0,B1,k1,r1)
    print("El nuevo mínimo es: ", minVal)

    return k1, B1


def orgFun2(k1,B1,r1,x):
    limD_X = 16.0
    limS_Y = 50.0
    limInf_Y = -115




    xrange = np.linspace(1,4,300)
    maximo1 = np.max(n(xrange,B1,k1,r1))
    print("El máximo está en f1(x) = ", maximo1)

    xrange = np.linspace(4,7,300)
    minimo1 = np.min(n(xrange,B1,k1,r1))
    print("El mínimo está en f1(x) = ", minimo1)


    valorIgualEn0 = 21

    for val in x:
        if np.abs(n(val,B1,k1,r1) -  np.abs(n(0,B1,k1,r1))) < 20:
            valorIgualEn0 = val
    print("El valor de x donde f1(x) da igual a f(min) es : ", valorIgualEn0)


    k1= valorIgualEn0/limD_X
    B1 = limS_Y/maximo1

    minVal = n(0,B1,k1,r1)
    print("El nuevo mínimo es: ", minVal)

    return k1, B1


def orgFun3(k1,B1,r1,x):
    x=np.linspace(0,11,1000)
    limD_X = 16.0
    limS_Y = 50.0
    limInf_Y = -115




    xrange = np.linspace(1,4,300)
    maximo1 = np.max(n(xrange,B1,k1,r1))
    print("El máximo está en f1(x) = ", maximo1)

    xrange = np.linspace(4,7,300)
    minimo1 = np.min(n(xrange,B1,k1,r1))
    print("El mínimo está en f1(x) = ", minimo1)


    valorIgualEn0 = 21


    for val in x:
        if np.abs(n(val,B1,k1,r1) - n(0,B1,k1,r1)) < 300:
            valorIgualEn0 = val
    print("El valor de x donde f1(x) da igual a f(min) es : ", valorIgualEn0)





    k1= valorIgualEn0/limD_X
    B1 = limS_Y/maximo1

    minVal = n(0,B1,k1,r1)
    print("El nuevo mínimo es: ", minVal)

    return k1, B1

k1, B1 = orgFun1(k1,B1,r1,x)

k2, B2 = orgFun2(k2,B2,r2,x)

k3,B3 = orgFun3(k3,B3,r3,x)






axes.plot(x, n(x,B1,k1,r1), '-', label=r'Modo normal $m=m_{1}$. ',color="cadetblue")

axes.plot(x, n(x,B2,k2,r2), '-', label=r'Modo normal $m=m_{2}$.',color="crimson")

axes.plot(x, n(x,B3,k3,r3), '-', label=r'Modo normal $m=m_{3}$.',color="black")



#axes.plot(x, n(x,0.025,0.7,r2), '-', label=r'$f(x)$. Semilla: 2',color="crimson")
#axes.plot(x, n(x,0.00125,1,r3), '-', label=r'$f(x)$. Semilla: 3',color="black")



# Se ajustan demás detalles del gráfico.
axes.set_xlabel('x', fontsize=12)
axes.set_ylabel(r'$\eta (x)$: Desplazamiento vertical.', fontsize=12)
# axes.legend(loc='upper left')
axes.grid(True, linestyle='--')
axes.set_title(r'Modos normales con $m= m_{1}, m_{2}, m_{3}$', fontsize=14)
axes.legend()
plt.tight_layout()
plt.show()
fig.savefig('modosNormales.pdf')
