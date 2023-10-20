# Project_LO
## Project script for the Python course

The script *cut_water_molecules.py* takes PDB files containing protein and water molecules, calculates
distance from the protein to each water molecule and saves a new PDB file containing water molecules 
that are within a certain distance from the protein. 

All requirements for this script to run are stored in requirements.txt

After cloning the repository, please run

    pip install -r requirements.txt

to install the libraries required for running this script.

Input PDB files are needed for the script to run. Test PDB files are stored in the *test_data* folder and named
protein*.pdb.

To run the script, use the command: 

    python cut_water_molecules.py

The user will then be asked their desired cutoff distance for the water molecules. For testing
reasons, any number between 10 and 30 is reasonable.

Output PDB files will be stored in the *output_data* folder.



 
