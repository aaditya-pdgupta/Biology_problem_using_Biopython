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