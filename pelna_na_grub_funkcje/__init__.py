import os

from Bio.PDB import PDBParser, PDBIO, Select

class CoarseGrainSelect(Select):
    def accept_atom(self, atom):
        residue = atom.get_parent()
        # Dla puryn (A, G): N9, C2, C6
        if residue.get_resname() in ['A', 'G']:
            if atom.get_id() in ['N9', 'C2', 'C6']:
                return True

        # Dla pirymidyn (C, U): N1, C2, C4
        if residue.get_resname() in ['C', 'U']:
            if atom.get_id() in ['N1', 'C2', 'C4']:
                return True

        # Dla backbone: P, C4'
        if atom.get_id() in ['P', "C4'"]:
            return True

        return False
def convert_to_grub(output_file,structure):
    io = PDBIO()
    io.set_structure(structure)
    os.chdir("Struktury")
    io.save(output_file, select=CoarseGrainSelect())
