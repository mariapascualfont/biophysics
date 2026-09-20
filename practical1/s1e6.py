#!/usr/bin/env python

import argparse
import sys

from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser


argp = argparse.ArgumentParser(
    prog='Exercise 6',
    description='6. Id 4, but for disulphide bonds.'
)

argp.add_argument('required_file',
                   help='PDB file to analyze')

argp.add_argument('distance',
                   help='Threshold distance (Å) for a SG-SG contact')

args = argp.parse_args()

filename = args.required_file
d = args.distance

print ("\nSettings\n--------")

for k, v in vars(args).items():
    print ('{:10}:'.format(k), v)

print ("\nSettings, again\n---------------")    

#print the variables once assigned

print(filename, d)
print()  

MAXDIST = float(d)


pdb_parser = PDBParser(PERMISSIVE=1)
st = pdb_parser.get_structure('structure', filename)


select = []

for at in st.get_atoms():
    if at.id == 'SG' and at.get_parent().get_resname() == 'CYS':
        select.append(at)

# Sort selected atoms by chain id, then residue number (for the listing)
select.sort(key=lambda a: (a.get_parent().get_parent().id,
                            a.get_parent().id[1]))

print("CYS residues found (SG atoms)")
print(f"{'Chain':<6}{'Residue':<8}{'Atom':<6}")
for at in select:
    chain_id = at.get_parent().get_parent().id
    res_num = at.get_parent().id[1]
    print(f"{chain_id:<6}{res_num:<8}{at.id:<6}")

if not select:
    print("\nNo CYS residues found in the structure.")
    sys.exit(0)



nbsearch = NeighborSearch(select)
contacts = list(nbsearch.search_all(MAXDIST, level='A'))

# Sort contacts by chain/residue number of the first atom, then the second
contacts.sort(key=lambda pair: (
    pair[0].get_parent().get_parent().id,
    pair[0].get_parent().id[1],
    pair[1].get_parent().get_parent().id,
    pair[1].get_parent().id[1]
))

print("\nDisulphide bond candidates (SG-SG contacts)")


if not contacts:
    print("No disulphide bonds were found.")
else:
    header = f"{'#':<4}{'CYS 1':<12}{'CYS 2':<12}{'Distance (Å)':<12}"
    print(header)
    print("-" * len(header))

    for i, (at1, at2) in enumerate(contacts, start=1):
        chain1 = at1.get_parent().get_parent().id
        chain2 = at2.get_parent().get_parent().id
        res1 = at1.get_parent().id[1]
        res2 = at2.get_parent().id[1]
        distance = at1 - at2

        label1 = f"{chain1}:{res1}"
        label2 = f"{chain2}:{res2}"

        print(f"{i:<4}{label1:<12}{label2:<12}{distance:<12.2f}")