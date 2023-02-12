import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)

import os

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import Bio.PDB

parser = Bio.PDB.PDBParser()
structure = parser.get_structure('6x8j', '6x8j.pdb')

protein_model = structure[0]

for chain in protein_model:
    print(chain)

chain_A = protein_model['A']
res = chain_A[58]
res

res.get_unpacked_list()

def get_aa(file):
    '''Accepts a PDB files name (string) and returns a list of residues
    that occur in a peptide.
    
     >>> ('1abc.pdb') -> ['GLY', 'ALA', 'LYS']
    '''

    amino_acids = []  # empty list to add the amino acids to

    parser = Bio.PDB.PDBParser()
    structure = parser.get_structure('6x8j', '6x8j.pdb')
    pp = Bio.PDB.PPBuilder().build_peptides(structure[0])

    # go through each chain and residue and append the amino acid identity to the list
    for chain in pp:
        for res in chain:
            res_name = res.get_resname()
            amino_acids.append(res_name)
            
    return amino_acids 

amino_acids = get_aa('6x8j.pdb')

sns.countplot(x=amino_acids, color='C00')
plt.xticks(rotation=45)
plt.show()