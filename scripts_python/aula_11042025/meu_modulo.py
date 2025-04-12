curso = "Tecnologia em Geoprocessamento"
disciplina = "Introdução à Linguagem Python para Análise de Dados"
periodo = "III"
pi = 3.14159
#________
saudacao_2 = "Curso: Tecnologia em Geoprocessamento\nDisciplina: Introdução à Linguagem Python para Análise de Dados\nPeríodo: III"

#________
def saudacao(nome):
    print(f"Seja bem vindo à disciplina de Python, {nome}!")

#______
def soma(n1, n2):
    return n1 + n2
    
#________________
import math
def area_circulo(r):
    return math.pi * r ** 2
    
#_______________
def hipot(a, b):
    return math.sqrt(a ** 2 + b **2)


