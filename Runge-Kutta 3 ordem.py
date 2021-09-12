from math import * # importa os valores matemático
def rungekutta3(f,y,x,h): #define a função para calcular os valores do método
 k1=f(x,y)
 k2=lambda k1: f(x+h/2,y+h*k1/2)
 k3=lambda k2: f(x+h,y+2*h*k2(k1)-h*k1)
#valores de k1 , k2 , k3 para utilização do método
 return y + h*(k1+4*k2(k1)+k3(k2))/6
f = lambda x,y : x*y*y*y-y 
#caso deseja-se resolver outra equação, deve-se trocar a equação no lambda
a=float(input('valor de y0'))
b=float(input('valor de x0'))
c=float(input('valor de h0 intervalo que vai pular')) #armazena os valores iniciais
d=float(input('valor final'))
y0,x0,h,t=a,b,c,d
i=0
# RUNGE-KUTTA 3ª Ordem
# Exemplo de solução através do método de 3ª Ordem
print ('\t\t\t\tRunge-Kutta 3 Ordem\n\n')
while x0 <=t+h:
 yn = rungekutta3(f,y0,x0,h) #manda os valores para função
 print("t\t\t\t tentativa %d f(%2.2f)\t= %4.6f" % (i,x0,y0)) # mostra os resultados
 y0 = yn
 x0 +=h #acrescenta os valores para o próximo ciclo caso necessário
 i=i+1

