import os

import matplotlib.pyplot as plt
import numpy as np
from Bio.PDB import PDBParser
def structure_load(nazwa_czasteczki):
    if not nazwa_czasteczki.endswith('.pdb'):
        nazwa_czasteczki = nazwa_czasteczki.lower() + ".pdb"
    os.chdir("Struktury")
    parser = PDBParser(QUIET=True)
    struktura = parser.get_structure(nazwa_czasteczki, nazwa_czasteczki)
    os.chdir("..")
    return struktura

def read_CA(struktura):
    all_ca=[]
    for atom in struktura.get_atoms():
        if atom.get_name() == "CA":
            all_ca.append(atom.get_coord())
    return all_ca

def contact_map(tablica_ca, cuttoff = 8.0):
    num_atoms = len(tablica_ca)
    contact_map = np.zeros((num_atoms, num_atoms), dtype=int)
    for i in range(num_atoms):
        for j in range(num_atoms):
            if not i == j:
                distans = np.linalg.norm(tablica_ca[i] - tablica_ca[j])
                if distans <= cuttoff:
                    contact_map[i][j] = 1
    return contact_map

def visualization_contact_map(tablica_ca):
    contact_matrix = contact_map(tablica_ca)
    x,y = np.where(contact_matrix == 1)
    plt.figure(figsize = (8,8))
    plt.scatter(x,y,c='black', s=10, label = "wartość 1")
    plt.gca().invert_yaxis()
    plt.title("Contact map")
    plt.xlabel("CA")
    plt.ylabel("CA")
    plt.grid(color='black', linestyle='--',linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.show()








