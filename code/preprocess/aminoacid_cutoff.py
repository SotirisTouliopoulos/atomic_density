
import sys


"""
Run this script through bash with the following command:
for file in ./*.pdb ; do python3 aminoacid_cutoff.py ''$file'' ; done
"""

# Script to count the number of CA atoms in a PDB file and write the filename to cutoff.txt if the count is less than or equal to 50
# The resulted files are removed from the analysis

with open( sys.argv[1] , 'r' ) as file:
    atom_list = []
    for line in file:
        if line.startswith('ATOM'):
            atom = line[13:15]
            atom_list.append(atom)

aminoacid = 0
for i in range(len(atom_list)):
    if atom_list[i] == 'CA' :
        aminoacid +=1

if aminoacid <= 50:
    with open ( 'cutoff.txt' , 'a' ) as output :
        output.write( str(sys.argv[1]) + str('\n'))


