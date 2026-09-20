import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='PS 1 - Exercise 1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('PDB_file',
                    help='Required file for the program')
parser.add_argument('res1',
                    help='Residue 1')
parser.add_argument('res2',
                    help='Residue 2')

# Read command line into args

args = parser.parse_args()
       
# Print the parameters that has been read 
    
print ("\nSettings\n--------")

for k, v in vars(args).items():
    print ('{:10}:'.format(k), v)

print ("\nSettings, again\n---------------")    

#print the variables once assigned
file = args.PDB_file
residue_1 = args.res1
residue_2 = args.res2

print(file, residue_1, residue_2)    

#!/usr/bin/env python
#
""" Simple program to print distances between atoms """

from Bio.PDB.PDBParser import PDBParser
import numpy as np

parser = PDBParser()

st = parser.get_structure('PDB', file)

#Selection of Residue 1
res1 = st[0]["A"][residue_1]
#Selection of Residue 2
res2 = st[0]["A"][residue_2]

print("Residue 1 is", res1.get_resname())
print("Residue 2 is", res2.get_resname())

print("\nAtom1 Atom2 dist1 dist2\n-------------------------")
for at1 in res1.get_atoms():      # Replace get_atoms with get_atom if you get an Error!
    for at2 in res2.get_atoms():
        dist = at2 - at1     # Direct procedure with (-) to compute distances
        vector = at2.coord - at1.coord  # Or using numpy coordinates
        distance = np.sqrt(np.sum(vector ** 2))
        print(at1, at2, dist, distance)

center = np.array([10, 10, 10])
print("\nDistance of res1 to {} \n".format(center))
for at1 in res1.get_atoms():
    vect = at1.coord - center
    distance = np.sqrt(np.sum(vect ** 2))
    print(at1, distance)

