import numpy as np
from Bio import PDB
from matplotlib import pyplot as plt

from zadanie_1_funkcje import structure_load
from Bio.PDB.vectors import calc_dihedral
def calculate_phi_psi(struktura):
    phi_angels = []
    psi_angels = []
    parser = PDB.PPBuilder()
    for pp in parser.build_peptides(struktura):
        for i in range(1,len(pp)-1):
            prev_residue = pp[i-1]
            current_residue = pp[i]
            next_residue = pp[i+1]
            try:
                n = current_residue["N"].get_vector()
                ca = current_residue["CA"].get_vector()
                c = current_residue["C"].get_vector()
                c_prev = prev_residue["CA"].get_vector()
                n_next = next_residue["N"].get_vector()
                psi = calc_dihedral(n, ca, c ,n_next)
                phi = calc_dihedral( c_prev,n,ca,c)
                psi_angels.append(np.degrees(psi))
                phi_angels.append(np.degrees(phi))
            except KeyError:
                continue
    return phi_angels, psi_angels

def visualization_ramahandran_map(nazwa_czasteczki):
    struktura = structure_load(nazwa_czasteczki)
    phi, psi = calculate_phi_psi(struktura)
    plt.figure(figsize=(10,10))
    plt.scatter(phi,psi,label="kąty ramahandrana")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Wykres Ramachandrana", fontsize=16)
    plt.xlabel("Kąt phi (stopnie)", fontsize=14)
    plt.ylabel("Kąt psi (stopnie)", fontsize=14)
    plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.show()

