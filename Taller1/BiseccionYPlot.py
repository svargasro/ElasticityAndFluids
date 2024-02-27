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

print("La raíz 1 por método de bisección es x= ",r1)
print("La raíz 2 por método de bisección es x= ",r2)
print("La raíz 3 por método de bisección es x= ",r3)


# comment #####################################################################


def n(x,B,k,m):
#    return B*(np.cosh(k*x)-np.cos(k*x) - ((np.cosh(m)-np.cos(m))/(np.sinh(m)-np.sin(m)))*(np.sinh(k*x)+np.sin(k*x)))
    return B*(np.cosh(m)-np.cos(m))*(np.sinh(k*x)+np.sin(k*x))- (np.sinh(m)- np.sin(m))*(np.cosh(k*x)+np.cos(k*x))

x = np.linspace(0,7,500)

plt.style.use('seaborn-v0_8')

fig, axes = plt.subplots(figsize=(6, 7))

axes.plot(x, n(x,1,1,r1), '-', label=r'$f(x)$. Semilla: 1',color="cadetblue")
axes.plot(x, n(x,1,1,r2), '-', label=r'$f(x)$. Semilla: 2',color="crimson")
axes.plot(x, n(x,1,1,r3), '-', label=r'$f(x)$. Semilla: 3',color="black")



# Se ajustan demás detalles del gráfico.
axes.set_xlabel('x', fontsize=12)
axes.set_ylabel(r'$f(x)$: Densidad de probabilidad.', fontsize=12)
# axes.legend(loc='upper left')
axes.grid(True, linestyle='--')
axes.set_title("Aproximación a funciones densidad \n de probabilidad para semillas 1,2 y 5.", fontsize=14)
axes.legend()
plt.tight_layout()
plt.show()
fig.savefig('modosNormales.pdf')





plt.show()
