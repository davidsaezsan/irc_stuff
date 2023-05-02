import re

# Read the Gaussian output file
with open('gaussian_output.log', 'r') as f:
    output = f.read()

# Define a regular expression pattern to match the converged geometries
pattern = re.compile(r'Input orientation:[\s\S]*?(?=Rotational constants)')

# Find all matches in the output file
matches = pattern.findall(output)

# Write each match to a separate file
for i, match in enumerate(matches):
    with open(f'converged_geometry_{i+1}.xyz', 'w') as f:
        # Extract the atom coordinates from the match
        atom_lines = match.split('\n')[5:-41]
        #Get rid of columns 0 and 2 without relevant info
        atom_lines2=[atom_lines[j].split()[1]+' '+atom_lines[j].split()[3]+' '+atom_lines[j].split()[4]+' '+atom_lines[j].split()[5] for j in range(len(atom_lines))]
        coords = '\n'.join(atom_lines2)
        
        # Write the coordinates to the output file
        f.write(f'{len(atom_lines)}\n\n{coords}\n')
