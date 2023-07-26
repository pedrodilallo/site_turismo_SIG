import pandas as pd
import sys
import os
from time import sleep
import itertools
import threading
import networkx as nx
from matplotlib import pyplot as plt
import PyQt5

sys.path.append('/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/')
import construtive_heuristic as ch
import local_search as ls


def importar_instancia(instance):
    path = '/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/'

    a  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/a.csv',  na_values = "0").fillna(0)
    b  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/b.csv',  na_values = "0").fillna(0) 
    c  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/c.csv',  na_values = '0').fillna(0) 
    d  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/d.csv',  na_values = "0").fillna(0) 
    e  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/e.csv',  na_values = "0").fillna(0) 
    h  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/H.csv',  na_values = "0").fillna(value = 0).iloc[:,1:].rename(columns = {"Unnamed: 1": "Unnamed: 0"})
    p  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/p.csv',  na_values = "0").fillna(0)
    pk = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/pk.csv', na_values = "0").fillna(0)
    r  = pd.read_csv(f'/home/pedropdl/Documents/graduacao/IC-PO/MOPTW/{instance}/R.csv',  na_values = "0").fillna(value = 0).iloc[:,1:].rename(columns = {"Unnamed: 1": "Unnamed: 0"})

    c  = c.set_index("Unnamed: 0")
    a  = a.set_index("Unnamed: 0")
    b  = b.set_index("Unnamed: 0")
    e  = e.set_index("Unnamed: 0")
    pk = pk.set_index("Unnamed: 0")


    for t in range(51):
        animate(t,instance,'construtiva')
  


    os.system('clear')

    incumbent_route = ch.construtive_heuristic(r,h,c,a,b,e,d,p,pk)

    
    print(100*"-")
    
    loading(50)

    print("Esta é sua rota incial: \n\n\n",incumbent_route)

    print('\n\nExecutando Busca Local...')

    print(100*"-")

    optimized_route = ls.local_search_loop(incumbent_route,a,b,c,d,e,p,pk,h,r,instance,name = "Unnamed: 0")

    print("Esta é sua rota otimizada: \n")
    print(f"Otimização Completa: \n[{'#'*48}]100%\n")
    print(optimized_route,'\n')
    print(100*'-')


def loading(percentage):
    done = int(percentage/2)*"#"
    in_progress = int((100-percentage)/2)*"-"
    print("Rota em otimização: \n",f'[{done}{in_progress}]{percentage}%\n')



def animate(percentage,instance,etapa):
    if etapa == "construtiva":
        done = int(percentage/2)*"#"
        in_progress = int((100-percentage)/2)*"-"
        
        for c in (['|', '/', '-', '\\']):
            string =100*'-' + "\n "+ f'Você escolheu a cidade: {instance}\n' + f"\rRota em otimização: \n [{done}{in_progress}]{percentage}%" + c + "\n" + "Importando Dados...\n" + 100*'-' 
            sys.stdout.write(string)
            sleep(0.01)
            os.system('clear')

