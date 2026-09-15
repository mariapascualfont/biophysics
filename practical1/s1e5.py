#!/usr/bin/env python


import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='Exercise 1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )


parser.add_argument('required_file',
                    help='Required file for the program')

parser.add_argument(
                    '--cd', 
                    dest='cutoff_distance',
                    help='Custoff Distance (default 2.5)'
                    )

args = parser.parse_args()
       

filename = args.required_file
cd = 2.5
if args.cutoff_distance:
    cd = args.cutoff_distance


# ---------------------------------

from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser

parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ', filename)


for model in st:
    for chain in model:

        # Get residues from this chain
        residues = list(chain.get_residues())

        # Check adjacent residues
        for res1, res2 in zip(residues[:-1], residues[1:]):

            # Make sure both residues contain C and N atoms
            if "C" not in res1 or "N" not in res2:
                continue

            c_atom = res1["C"]
            n_atom = res2["N"]

            # Calculate C-N distance
            bond_distance = c_atom - n_atom

            # Only print if distance is below cutoff
            if bond_distance < cd:
                print(
                    f"Bond between {res1.resname}{res1.id[1]} (C) and "
                    f"{res2.resname}{res2.id[1]} (N): "
                    f"{bond_distance:.2f} Å"
                )
