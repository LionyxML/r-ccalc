#!/usr/bin/python3
# Arquivo : rccalc.py
# Programa: Calculadora de operações básicas em números
#           complexos
# Autor   : Rahul Martim Juliato
# Versão  : 0.1  -  09.04.2018
#         : 0.2  -  10.04.2018 - Suporte à notação de engenharia


# Bibliotecas
import os
import math
import cmath


if os.name == 'posix':
    limpa_tela = 'clear'
else:
    limpa_tela = 'cls'

def clear():
    os.system(limpa_tela)


def sinalizacao(analisado):
    if analisado >= 0:
        return '+'
    else:
        return ''


    
def intro():
    print('''
Calculadora de Números Complexos
       ____ ____    _    _     ____ 
 _ __ / ___/ ___|  / \  | |   / ___|
| '__| |  | |     / _ \ | |  | |    
| |  | |__| |___ / ___ \| |__| |___ 
|_|   \\____\\____/_/   \_\\_____\\____|
                                    
Rahul Martim Juliato (2018)
''')


def prompt(frase="", tiponum=False):
    if len(frase):
        print(frase)

    if tiponum is True:
        while True:
            try:
                valor=float(input("rCCALC>>> "))
                break;
            except:
                print("Opa, estou esperando um número, tente novamente!")

    else:
        valor=input("rCCALC>>> ")

    return valor


# Snipet para conversão em números de engenharia
from math import floor, log10

def powerise10(x):
    """ Returns x as a*10**b with 0 <= a < 10
    """
    if x == 0: return 0,0
    Neg = x < 0
    if Neg: x = -x
    a = 1.0 * x / 10**(floor(log10(x)))
    b = int(floor(log10(x)))
    if Neg: a = -a
    return a,b

def eng(x):
    """Return a string representing x in an engineer friendly notation"""
    a,b = powerise10(x)
    if -3 < b < 3: return "%.4g" % x
    a = a * 10**(b % 3)
    b = b - b % 3
    return "%.4gE%s" % (a,b)
## Fim do Snipet


def menu():
    print('''
Opções:

0) Sair
1) Converter Retangular para Polar
2) Converter Polar para Retangular
3) Operações Matemáticas

''')


def retppol():

    retan=complex()
    resp='nope'

    
    while resp != '0':
        clear()
        
        real = prompt("Entre com o valor da parte real: ", tiponum=True)
        print('')
        comp = prompt("Entre com o valor da parte imaginária: ", tiponum=True)
        print('')
        
        retan = real+(0 + 1j)*comp
        polar = cmath.polar(retan)


        sinal=sinalizacao(comp)

        print("%s %s%sj = %s |_%s°\n"%(retan.real, sinal, retan.imag, eng(polar[0]), eng(math.degrees(polar[1]))))

        resp=prompt("Pressione <ENTER> para outra conversão, '0' para sair")


def polpret():

    retan=complex()
    resp='nope'

    
    while resp != '0':
        clear()
        
        modul = prompt("Entre com o valor do módulo: ", tiponum=True)
        print('')
        angul = prompt("Entre com o valor do ângulo (graus): ", tiponum=True)
        print('')

        
        retan = cmath.rect(modul,math.radians(angul))
    
        sinal=sinalizacao(retan.imag)
        
        print("%s |_%s° = %s %s%sj\n"%(modul, angul, eng(retan.real), sinal, eng(retan.imag)))

        resp=prompt("Pressione <ENTER> para outra conversão, '0' para sair")


        
def formatador():
    opcao = prompt('''\nQual o formato do número?
r - Retangular
p - Polar
''')
    while opcao not in ['r','p']:
        opcao = prompt("Entre com uma opção válida, 'r' ou 'p'")

    if opcao == 'r':
        real = prompt("Entre com o valor da parte real: ", tiponum=True)
        print('')
        imag = prompt("Entre com o valor da parte imaginária: ", tiponum=True)
        print('')

        return real + (0 + 1j) * imag

    if opcao == 'p':
        modul = prompt("Entre com o valor do módulo: ", tiponum=True)
        print('')
        angul = prompt("Entre com o valor do ângulo (graus): ", tiponum=True)
        print('')

        return cmath.rect(modul,math.radians(angul))
    

def imprime_op(operando,texto=""):
    operacao=operando
    print("%s: %s %s%sj = %s |_%s°\n" % (texto,eng(operacao.real), sinalizacao(operacao.imag), eng(operacao.imag), eng(cmath.polar(operacao)[0]), eng(math.degrees(cmath.polar(operacao)[1]))))



def operacoes():
    clear()
    print("Entre com o primeiro número:")
    num1=formatador()
    clear()
    print("Entre com o segundo número:")
    num2=formatador()
    clear()

    imprime_op(num1, "Número 1     ")
    imprime_op(num2, "Número 2     ")
    imprime_op(num1+num2,"Soma         ")
    imprime_op(num1-num2,"Subtração    ")
    imprime_op(num1*num2,"Multiplicação")
    imprime_op(num1/num2,"Divisão      ")
    
    prompt()

        
    
def main():
    selecao = 1

    while selecao != "0":
        clear()
        intro()
        menu()
        selecao=prompt()

        if selecao == "1":
            retppol()
        elif selecao =="2":
            polpret()
        elif selecao =="3":
            operacoes()
            

# Sequência principal
clear()
intro()
main()

