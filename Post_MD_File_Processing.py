##https://colab.research.google.com/drive/1mJR42vffI8FVxaiaw5cyAISicAZ4jsyB#scrollTo=-CfU7CNq-U8r

pip install biopython
from google.colab import files

# ===== Upload PDB =====
uploaded = files.upload()
pdb_filename = list(uploaded.keys())[0]

# ===== Peptide sequence input =====
peptide_seq = input("Enter peptide sequence (one-letter code): ").strip().upper()

# ===== Mapping table with histidine variants etc. =====
aa_map = {
    'A': ['ALA'],
    'R': ['ARG'],
    'N': ['ASN'],
    'D': ['ASP'],
    'C': ['CYS'],
    'Q': ['GLN'],
    'E': ['GLU'],
    'G': ['GLY'],
    'H': ['HIS', 'HIE', 'HID', 'HIP'],
    'I': ['ILE'],
    'L': ['LEU'],
    'K': ['LYS', 'LYN'],
    'M': ['MET'],
    'F': ['PHE'],
    'P': ['PRO'],
    'S': ['SER'],
    'T': ['THR'],
    'W': ['TRP'],
    'Y': ['TYR'],
    'V': ['VAL']
}

# Build all possible resname patterns for peptide
target_variants = [aa_map[aa] for aa in peptide_seq]

# Residues to remove: water and ions
remove_resnames = {"WAT", "HOH", "NA", "NA+", "CL", "CL-"}

def assign_peptide_chain(input_pdb, output_pdb, target_variants, protein_chain='A', peptide_chain='X'):
    with open(input_pdb, 'r') as f:
        lines = f.readlines()

    # Extract residue sequence from ATOM/HETATM lines
    residues = []
    for line in lines:
        if line.startswith(("ATOM", "HETATM")):
            resname = line[17:20].strip()
            resnum = int(line[22:26])
            if not residues or residues[-1][0] != resnum:
                residues.append((resnum, resname))

    # Search for peptide match
    match_start = None
    for i in range(len(residues) - len(target_variants) + 1):
        if all(residues[i+j][1] in target_variants[j] for j in range(len(target_variants))):
            match_start = residues[i][0]
            break

    if match_start is None:
        raise ValueError("❌ Peptide sequence not found in PDB.")

    peptide_resnums = {residues[i][0] for i in range(len(residues))
                       if match_start <= residues[i][0] < match_start + len(target_variants)}

    # Modify chain IDs and remove unwanted residues
    new_lines = []
    for line in lines:
        if line.startswith(("ATOM", "HETATM")):
            resname = line[17:20].strip()
            resnum = int(line[22:26])

            # Skip water and ions
            if resname in remove_resnames:
                continue

            # Assign chain
            if resnum in peptide_resnums:
                line = line[:21] + peptide_chain + line[22:]
            else:
                line = line[:21] + protein_chain + line[22:]

        new_lines.append(line)

    with open(output_pdb, 'w') as f:
        f.writelines(new_lines)

    print(f"✅ Saved {output_pdb} — protein → {protein_chain}, peptide → {peptide_chain}, removed WAT/NA+/CL-")

# ===== Run =====
output_filename = "complex2.pdb"
assign_peptide_chain(pdb_filename, output_filename, target_variants)
files.download(output_filename)
