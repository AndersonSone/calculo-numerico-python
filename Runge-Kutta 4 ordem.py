from math import *
def RungeKutta4(f,y,x,h):#para calcular o valor inicial
 k1 = h*f(x,y)
 k2 = lambda k1: h*f(x + h/2, y + k1/2)
 k3 = lambda k2: h*f(x + h/2, y + k2(k1)/2) #os valores para uso do método do RK4
 k4 = lambda k3: h*f(x+h,y + k3(k2))
 return y + (k1+2*k2(k1)+2*k3(k2)+k4(k3))/6
f = lambda x,y : -x*x*y*y+y
#obs: caso deseja-se resolver outra equação, deve-se trocar a equação no lambda
a=float(input('valor de y0'))
b=float(input('valor de x0'))
c=float(input('valor de h0 intervalo que vai pular')) # digita e armazena os valores iniciais
d=float(input('valor de x que deve ser calculada'))
y0,x0,h,t=a,b,c,d #armazena os valores nessas variavel
i=0
# RUNGE-KUTTA 4ª Ordem
# Exemplo de solução através do método de 4ª Ordem
print ('\n\n\t\t\t\tRunge-Kutta 4 Ordem\n\n')
while x0 <t+h:
 yn = RungeKutta4(f,y0,x0,h)
 print("\t\t\t\tpasso %d f(%2.6f)\t= %4.6f" % (i,x0,y0)) #imprime os valores
 y0 = yn
 x0 +=h
 i=i+1
