# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:28:41 2026

@author: sandr
"""
from pathlib import Path

pasta=Path.cwd()
idx=0
print("ORGANIZADOR DE FICHEIROS")
print("----------------------- ")


for ficheiro in pasta.iterdir():
    if ficheiro.is_file():
        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)
        print("------------------------")
        idx=idx+1
    else:
        print("A pasta não contém ficheiros.")
        
    total_ficheiros = idx
    print(f" {total_ficheiros} Ficheiros encontrados")
    
