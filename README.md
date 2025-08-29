AIoptide: An AI-Driven Pipeline for Peptide Optimization

AIoptide is a modular, scalable workflow designed for rational optimization of protein–peptide complexes. Leveraging AI-based screening, in-house structural modeling, MD simulations, and machine learning–based affinity scoring, AIoptide streamlines the discovery of peptide candidates with enhanced stability and binding potential—accelerating therapeutic and diagnostic developments.

Workflow Modules

Peptide Library Generation

Enables systematic mutagenesis (class‑wise or all‑residue) to create large peptide variant libraries.

Run via Google Colab [Peptide Library Generation Notebook].

Peptide Preprocessing & Stability Filtering

Removes duplicates, maintains consistent peptide lengths, and enables GRAVY‑based stability evaluation.

Accessible via [Peptide Preprocessing Notebook].

Binding Affinity Prediction (PBEE)

Estimates peptide–protein binding free energies (ΔG) using a machine learning model built on Rosetta descriptors 
ks.uiuc.edu
+10
GitHub
+10
Google Colab
+10
arXiv
+7
arXiv
+7
Nature
+7
ks.uiuc.edu
.

After MD simulations, use this for quantitative scoring of candidate complexes.

Run PBEE via [PBEE Affinity Prediction Notebook].

Google Colab Notebooks
Module	Colab Link
Peptide Library Generation	Notebook
Peptide Preprocessing	Notebook
Binding Affinity Prediction	PBEE Notebook
Case Studies

AIoptide was validated using four native protein–peptide complexes:

Case	PDB ID	Context
1	1T63	Androgen Receptor – GRIP1 peptide
2	1T5Z	Androgen Receptor – ARA70 peptide
3	1X7J	Estrogen Receptor β – Coactivator
4	3O34	p53 – Coactivator peptide

Each case folder includes library files, screening outputs, structural models, MD trajectories, and PBEE results.

How to Use

Clone the repository:

git clone https://github.com/Computational-biolab/AIoptide.git
cd AIoptide


Access and run the relevant Google Colab notebook for the desired module.

Review case study folders for reproducibility or adaptation for your target system.

Citation

If used in your work, please cite:
Sharma, P., et al. AIoptide: An AI-driven pipeline for peptide optimization. (2025).

Also, for PBEE:
Chaves, E. J. F., et al. Estimating Absolute Protein–Protein Binding Free Energies by a Super Learner Model. J. Chem. Inf. Model. 2025
