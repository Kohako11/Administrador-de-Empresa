#Criando alguma coisa com class

import os
import time
from turtle import title


class Funcionario:
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    def aumento(self):
        print('Ok, passe as informações!')
        valor_do_aumento = int(input('Coloque o valor do aumento:'))
        self.aumentar_salario(valor_do_aumento)
    
    def aumentar_salario(self, aumento):
        self.salario += aumento

    def exibir_funcionarios(self):
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Cargo: {self.cargo}
Salário: ${self.salario:.2f}
''')

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def lista_de_funcionarios(self):
        if self.funcionarios:
            print(f'Estes são os funcionários da empresa {self.nome}')
            for funcionario in self.funcionarios:
                print(funcionario.nome)
        else:
            print(f'A {self.nome}não possui nenhum funcionário no momento!')
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'O {funcionario.nome} foi adicionado a lista de empregados da {self.nome}')
    
    def remover_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f"{funcionario.nome} foi removido de {self.nome}")
        else:
            print(f"{funcionario.nome} não é um funcionário de {self.nome}")

def Gerir_empresa():
    empresa = Empresa(input('Digite o nome de sua empresa:').title())
    
    while True:
        print('''
    Olá, bem-vindo ao programa 
        'Administre Já'

Temos as seguintes opções:

1 - Empresa(E)
2 - Funcionários(F)
3 - Sair(S)
''')
        escolha = input('Digite o qual função quer utilizar:').upper()
        
        if escolha == 'E':
            print('Ok, você escolheu funções Empresa!')
            print('''

        Empresa

Temos as seguintes opções:
1 - Adicionar funcionário(A)
2 - Remover funcionário(R)
3 - Ver funcionários(V)
''')
            função = input('Digite a função:').upper()
            if função == 'A':
                nome = input("Digite o nome do funcionário: ").title()
                idade = int(input("Digite a idade do funcionário: "))
                cargo = input("Digite o cargo do funcionário: ")
                salario = float(input("Digite o salário do funcionário: "))

                novo_funcionario = Funcionario(nome, idade, cargo, salario)
                empresa.adicionar_funcionario(novo_funcionario)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif função == 'R':
                remover_funcionário = input('Digite o nome do fncionário:').title()
                for funcionário in empresa.funcionarios:
                    if funcionário.nome == remover_funcionário:
                        empresa.remover_funcionario(funcionário)
                        os.system('cls' if os.name == 'nt' else 'clear')
            
            elif função == 'V':
                empresa.lista_de_funcionarios()
                time.sleep(10)
                os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 'F':
            print('''
        
        Funcionário

Temos as seguintes opções:
1 - Aumentar o salário(A)
2 - Exibir Funcionário(E)
''')
            função = input('Digite a função:').upper()
            if função == 'A':
                nome_do_funcionário = input('Digite o nome do funcionário:').title()
                for funcionário in empresa.funcionarios:
                    if funcionário.nome == nome_do_funcionário:
                        aumento = float(input('Digite o valor do aumento:'))
                        funcionário.aumentar_salario(aumento)
                        print(f"Salário de {funcionário.nome} aumentado para ${funcionário.salario:.2f}")
                        os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print(f'O nome {nome_do_funcionário} não foi encontrado')
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif função == 'E':
                nome_do_funcionário = input('Digite o nome do funcionário:')
                for funcionário in empresa.funcionarios:
                    if funcionário.nome == nome_do_funcionário:
                        funcionário.exibir_funcionarios()
                        time.sleep(10)
                        os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print(f'O nome {nome_do_funcionário} não foi encontrado')
                    os.system('cls' if os.name == 'nt' else 'clear')

        else:
            print('O programa encerrará!')
            time.sleep(7)
            break

Gerir_empresa()
