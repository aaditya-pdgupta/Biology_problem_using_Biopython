import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)

import os

import matplotlib.pyplot as plt
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
#plt.show()
plt.savefig("examined_amino_acid_frequency.pdf", dpi=400,  bbox_inches='tight')

def get_helix_start(file):
    '''Accepts a PDB files name (string) and returns a list of residues
    that occur at the start of a helix.
    
     >>> ('1abc.pdb') -> ['GLY', 'ALA', 'LYS']
    '''
    
    AA_list = []
    
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('HELIX'):
                AA_list.append(line[15:18])
    
    return AA_list

def get_sheet_start(file):
    '''Accepts a PDB files name (string) and returns a list of residues
    that occur at the start of a sheet.
    
     >>> ('1abc.pdb') -> ['GLY', 'ALA', 'LYS']
    '''
    
    AA_list = []
    
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('SHEET'):
                AA_list.append(line[17:20])
    
    
    return AA_list

path, _ = os.path.split(os.getcwd())
top80 = os.path.join(path, 'Top80')

helix_start = []
sheet_start = []
general = []

for file in os.listdir(top80):
    if file.endswith('pdb'):
        helix_start.extend(get_helix_start(os.path.join(top80,file)))
        sheet_start.extend(get_sheet_start(os.path.join(top80,file)))
        general.extend(get_aa(os.path.join(top80,file)))

sns.countplot(x=helix_start, palette='viridis')
plt.xticks(rotation=90)
plt.show()