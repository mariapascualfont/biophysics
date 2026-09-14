"""Example script for building custom command-lines use argparse"""

import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='ProgName', 
                                 description='Description of the program'
                                 )

# Use add_argument for all needed arguments
# https://docs.python.org/3/library/argparse.html

# Fornat for a boolean parameter, value stored as True if present, False if not
parser.add_argument(
                    'required_file', 
                    )

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    'residue_type',
                    help= 'ns' 
                    )


# Read command line into args

args = parser.parse_args()
       
# Print the parameters that has been read 
    
print ("\nSettings\n--------")

for k, v in vars(args).items():
    print ('{:10}:'.format(k), v)

print ("\nSettings, again\n---------------")    

filePDB = args.required_file    
residue = args.residue_type
with open(filePDB, 'r') as file:
    for line in file:
        if line.startswith('ATOM'):
            residue_number = line[17:20].strip()
            atom = line[12:16].strip()
            if atom == 'CA' and residue_number == residue:
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])

                print(f'atom number {line[9:11]} , x:{x}, y:{y}, z:{z}')