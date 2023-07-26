import os
import importar_cidade
import pandas as pd
import sys
sys.path.append('/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/')
def menu():
    os.system('clear')
    print(100*"-")
    print("Escolha a cidade:")
    instances = ['small_instances/rc1/101/2D/C2', 'small_instances/rc1/106/3D/C3',
                 'small_instances/rc1/106/2D/C3', 'small_instances/r1/101/3D/5N',
                 'small_instances/c1/108/1D/C3' ,'small_instances/rc1/106/3D/C1',
                 'small_instances/c1/108/3D/C1' ,'small_instances/r1/101/3D/11N',
                 'small_instances/r1/101/2D/10N', 'small_instances/rc1/106/1D/C2',
                 'small_instances/c1/107/2D/C3' ,'small_instances/c1/108/2D/C3',
                 'small_instances/rc1/107/1D/C1', 'small_instances/c1/108/1D/C1',
                 'small_instances/rc1/107/1D/C2', 'small_instances/r1/101/2D/6N',
                 'small_instances/c1/107/1D/C3' ,'small_instances/rc1/107/3D/C2',
                 'small_instances/r1/101/3D/18N', 'small_instances/r1/101/3D/21N',
                 'small_instances/rc1/107/3D/C3', 'small_instances/rc1/106/3D/C2']
    n = 1
    for i in instances:
        print(f"{n} - {i}")
        n = n+1

    cidade_escolhida = ''
    lista_n = list(range(1,n))
    print(100*"-")


    print("Digite o Número da cidade escolhida:\n")

    while cidade_escolhida not in lista_n:
        try:
            cidade_escolhida = int(input())
        except:
            print(f"Erro: digite um número entre 1 e {n-1}")

    os.system('clear')

    print(100*"-",'\n')

    print(f"Você escolheu a cidade: {cidade_escolhida}\n")

    
    print(100*"-",'\n')

    importar_cidade.importar_instancia(instances[cidade_escolhida])




menu()