import os
from Bio.PDB import PDBIO, Select

class CoarseGrainSelect(Select):
    def accept_atom(self, atom):
        residue = atom.get_parent()
        atom_name = atom.name.strip()
        residue_name = residue.get_resname().strip()

        # For purines (A, G): N9, C2, C6
        if residue_name in ["A", "G"]:
            if atom_name in ["N9", "C2", "C6"]:
                return True

        # For pyrimidines (C, U): N1, C2, C4
        if residue_name in ["C", "U"]:
            if atom_name in ["N1", "C2", "C4"]:
                return True

        # For backbone: P, C4'
        if residue_name in ["A", "C", "G" , "U"]:
            if atom_name in ["P", "C4'"]:
                return True

        return False

def convert_to_grub(output_file, structure):
    io = PDBIO()
    io.set_structure(structure)
    os.chdir("Struktury")
    io.save(output_file, select=CoarseGrainSelect())
