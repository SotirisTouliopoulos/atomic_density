

"""
Run this script through bash with the following command:
for file in ./*.pdb ; do python3 mutate_pdb_format.py ''$file'' >> ''$file''.mutated  ; done
"""

# Script that converts HETATM records from crystallographic water to ATOM records.
# It is used before solvating structures to avoid issues

import sys

try:    
    with open(sys.argv[1], 'r') as file:
        for line in file:
            
            if line.startswith('ATOM'):
                if line[16] == 'A' or line[16] == ' ' :
                    print(line[:-1])
        
            elif line.startswith("HETATM"):
                residue = line[17:20] 
                if residue == "HOH":
                    atom_number = line[6:13]
                    print("ATOM ", atom_number, line[14:-1])
                    
                else:
                    print(line[:-1])
        
except:
    print("error in mutating")            
            