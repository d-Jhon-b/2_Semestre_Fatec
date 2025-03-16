import os
import math

def calcIMC(a, b):
    res = a/(math.pow(b,2))
    return res
def inputs():
    try:
        peso = float(input('insira o seu peso: \n'))
        altura = float(input('insira a sua altura: \n'))

        print(f'Seu IMC é de: {calcIMC(peso, altura):.2f}') 
    except ValueError:
        print(f'O erro do programa foi em:\n{ValueError}')

inputs()