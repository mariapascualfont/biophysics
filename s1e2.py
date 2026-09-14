#!/usr/bin/env python


import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='Exercise 1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )


parser.add_argument('required_file',
                    help='Required file for the program')

parser.add_argument('residue',
                    help='Residue number')


parser.add_argument(
                    '--chain', 
                    dest='chain',
                    help='Chain number (if applicable)'
                    )

args = parser.parse_args()
       

filename = args.required_file
r = float(args.residue)
c = args.chain


# ---------------------------------


""" Simple program to print ARG residues iteration over atoms """

from Bio.PDB.PDBParser import PDBParser

parser = PDBParser()

st = parser.get_structure('1UBQ', filename)


selected = []

for residue in st.get_residues():

    # Residue number is stored in residue.id[1]
    if residue.id[1] == r:

        # If a chain was specified, check the chain
        if c is None or residue.get_parent().id == c:
            selected.append(residue)

# Print the atoms
print("Atoms:")

for residue in selected:
    for atom in residue.get_atoms():
        print(
            f"{residue.get_resname()}, "
            f"{residue.id}, "
            f"{atom.get_name()}, "
            f"{atom.get_coord()}"
        )