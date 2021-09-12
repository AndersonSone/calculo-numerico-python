from math import* #importar os valores matemático como seno exponencial
#na parte de return irá colocar a função para calcula e retorna o valor
def fun(x,y): 
 return -x*x*y*y+y #colocar a função desejada para realização do cálculo casodesejado só trocar a função
#declarar os valores iniciais e passos dados no exercício
x_inicial=float(input('valor inicial para x'))
x_final=float(input('valor de x final cujo o y se queira sabe')) #inserir os valoresdado de x , y , xfinal e passo
y_inicial=float(input('valor inicial de y0'))
h=float(input('valor de passos'))
xn=x_inicial #transferir os valores para xn e yn para ser usado
yn=y_inicial
xn1=xn+h #acrescenta o novo valor do intervalo para h
i=0 #usado para saber os números de passos
while xn<x_final:
 i=i+1 #adição para saber o número de passo
 k1=fun(xn,yn) #primeira função, para ter os valores da função
 k2=fun(xn1,yn+h*k1) #segunda função
 yn1=yn+(h/2)*(k1+k2) #através do teorema para encontrar o yn1
 yn=yn1 #transferi para o yn assim para realiza o novo ciclo
 xn+=h
 xn1+=h #coloca nos dois o intervalo
 print("\t\t\t\tf(%4.6f)=%4.6f"%(xn,yn)) #coloca na tela os valores encontrados
print("\n\n\t\t\t\ty(%2.2f)\t= %4.6f\n\n" % (xn,yn))# coloca na tela os últimos valoresencontrados

