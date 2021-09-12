from math import * 
def fun(x,y): 
 return -x*x*y*y+y #-x*x*y*y+y x*y*y*y-y #aqui coloca a função desejada
# caso deseja-se resolver outra equação, deve-se trocar a equação no return
#na parte de return irá coloca a função para calcula e retorna o valor
x_inicial=float(input('valor inicial para x'))
x_final=float(input('valor de x final cujo o y se queira sabe')) # aba para colocar os
#valores iniciaias x , y ,x final e passo
y_inicial=float(input('valor inicial de y0'))
h=float(input('valor de passos'))
#declarar os valores iniciais e passos dados no exercício
xn=x_inicial
yn=y_inicial
while xn<x_final: # condição inicial estava parando 1 casa antes do que precisava
 yn1=yn+h*fun(xn,yn) #teorema de Euler
 yn=yn1
 xn+=h #adiciona o passo no X
 print("\t\t\t\tf(%.6f)=%.6f"%(xn,yn)) #imprime os valores conforme o passo escolhido
print("\n\n\t\t\t\ty(%2.2f)\t= %4.6f\n\n" % (x_final,yn)) #imprimi os valores finais
