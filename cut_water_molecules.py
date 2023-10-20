# Import libraries that are needed for this script to run
import os
import numpy as np
import prody as pd

# Define a function which calculates distance between protein and each water molecule 
def water_distance(structure, cutoff_distance): 
    protein_atoms = structure.select('protein') # Select protein atoms
    water_atoms = structure.select('water') # Select water atoms

    # Get coordinates of protein and water atoms
    protein_coords = protein_atoms.getCoords()
    water_coords = water_atoms.getCoords()

    # Use Euclidean norm to calculate distance between protein and each water molecule
    distances = np.linalg.norm(water_coords[:, np.newaxis] - protein_coords, axis=2)

    # Find water atoms within the cutoff distance from the protein
    within_cutoff = np.any(distances <= cutoff_distance, axis=1)
    close_waters = water_atoms[within_cutoff]

    return close_waters

# Ask the user what is their desired cutoff distance
cutoff_distance = float(input("Please enter your desired cutoff distance in Ångstroms: "))

# Find input PDB files that match the pattern "protein*.pdb"
input_folder = './test_data'
input_pdb_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.startswith("protein")]

# Decide where the output files will be saved
output_folder = './output_data'

# Check if the output folder exists - if not, then create it
os.makedirs(output_folder, exist_ok=True)

# Loop that applies water_distance function to each of the input pdb files
for pdb_file in input_pdb_files:
    # Load PDB file using ProDy
    structure = pd.parsePDB(pdb_file)

    # Find water molecules within wanted cutoff distance from the protein
    close_waters = water_distance(structure, cutoff_distance)

    # Write out water molecules to a new PDB file
    output_pdb_file = os.path.join(output_folder, f"cut_waters_{os.path.basename(pdb_file)}")
    pd.writePDB(output_pdb_file, close_waters)

    print(f"Water molecules within {cutoff_distance} Ångstroms from the protein in {pdb_file} "
          f"have been written to {output_pdb_file}")
    
    
