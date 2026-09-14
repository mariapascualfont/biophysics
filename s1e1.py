#!/usr/bin/env python


import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='Exercise 1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )


parser.add_argument('required_file',
                    help='Required file for the program')

parser.add_argument('distance',
                    help='Threshold distance')


args = parser.parse_args()
       

filename = args.required_file
d = args.distance


# ---------------------------------



from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser

MAXDIST = float(d)  

parser = PDBParser(PERMISSIVE=1)


st = parser.get_structure('1UBQ', filename)

select = []


for at in st.get_atoms():
    if at.id == 'CA':
        select.append(at)
        print(f"ATOM: {at.get_parent().get_resname()}, {at.get_parent().id[1]}, {at.id}")


nbsearch = NeighborSearch(select)

print("NBSEARCH:")


ncontact = 1

for at1, at2 in nbsearch.search_all(MAXDIST):
    print(f"Contact: {ncontact}")
    print(f"at1: {at1}, {at1.get_serial_number()}, {at1.get_parent().get_resname()}")
    print(f"at2: {at2}, {at2.get_serial_number()}, {at2.get_parent().get_resname()}")
    print()
    ncontact += 1