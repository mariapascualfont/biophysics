#!/usr/bin/env python

"""Example script for building custom command-lines use argparse"""

import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='PS 1 - Exercise 3', 
                                 description='Determine all possible hydrogen bonds (Polar atoms at less than 3.5 Å)'
                                 )

# Use add_argument for all needed arguments
# https://docs.python.org/3/library/argparse.html

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('PDB_file',
                    help='Required file for the program')
parser.add_argument('-d', '--cutoffdistance', type=float,
                    help='Distance threshold', default=3.5)

# Read command line into args

args = parser.parse_args()
       
# Print the parameters that has been read 
    
print ("\nSettings\n--------")

for k, v in vars(args).items():
    print ('{:10}:'.format(k), v)

print ("\nSettings, again\n---------------")    

#print the variables once assigned
file = args.PDB_file
distance = args.cutoffdistance

print(file, distance)    

#!/usr/bin/env python
#
""" Simple program to search contacts """

from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser

MAXDIST = float(distance)  # Define distance for a  contact

parser = PDBParser(PERMISSIVE=1)

# load structure from PDB file

st = parser.get_structure('PDB', file)

select = []

#Select only CA atoms

for at in st.get_atoms():
    if at.id in {'O', 'N', 'S'}:
        select.append(at)
        print(f"ATOM: {at.get_parent().get_resname()}, {at.get_parent().id[1]}, {at.id}")

# Preparing search
nbsearch = NeighborSearch(select)

print("NBSEARCH:")

#Searching for contacts under HBLNK

ncontact = 1

for at1, at2 in nbsearch.search_all(MAXDIST):
    print(f"Contact: {ncontact}")
    print(f"at1: {at1}, {at1.get_serial_number()}, {at1.get_parent().get_resname()}")
    print(f"at2: {at2}, {at2.get_serial_number()}, {at2.get_parent().get_resname()}")
    print()
    ncontact += 1
