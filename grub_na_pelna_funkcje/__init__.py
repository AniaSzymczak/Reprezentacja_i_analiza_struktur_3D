import os
from Bio import PDB
from Bio.PDB.Structure import Structure
from zadanie_1_funkcje import structure_load
from Bio.PDB import PDBParser, Superimposer, PDBIO

def save_to_file(struktura, output_name):
    os.chdir("Struktury")
    io = PDBIO()
    io.set_structure(struktura)
    io.save(output_name)

def convert_to_full(structure_name,output_name):
    structure = structure_load(structure_name)
    parser = PDBParser(QUIET=True)
    adenine_template = parser.get_structure("adenin", "templates/adenine.pdb")
    cytosine_template = parser.get_structure("cytosine", "templates/cytosine.pdb")
    guanine_template = parser.get_structure("guanine", "templates/guanine.pdb")
    uracil_template = parser.get_structure("uracil", "templates/uracil.pdb")
    dic = {
        "A": adenine_template[0]["A"][26],
        "C": cytosine_template[0]["A"][29],
        "G": guanine_template[0]["A"][24],
        "U": uracil_template[0]["A"][11],
    }
    nowa_struktura = Structure(output_name)
    for model in structure:
        nowyModel = PDB.Model.Model(model.id)
        nowa_struktura.add(nowyModel)
        for chain in model:
            nowy_chain = PDB.Chain.Chain(chain.id)
            nowyModel.add(nowy_chain)
            for residue in chain:
                full_atom_residue = dic[residue.get_resname().strip()].copy()
                full_atom_residue.id = (" ", residue.id[1], " ")
                atom_list_gruboziarnista = [atom for atom in residue]
                atomy_z_template = [full_atom_residue[atom.get_name()] for atom in atom_list_gruboziarnista]
                superimposer = Superimposer()
                superimposer.set_atoms(atom_list_gruboziarnista, atomy_z_template)
                for atom in full_atom_residue:
                    atom.transform(superimposer.rotran[0], superimposer.rotran[1])
                nowy_chain.add(full_atom_residue)
    save_to_file(nowa_struktura, output_name)