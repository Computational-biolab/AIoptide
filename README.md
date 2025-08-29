# AIoptide: An AI-Driven Pipeline for Peptide Optimization  

**AIoptide** is a modular and scalable computational framework for rational protein–peptide optimization.  
It integrates **AI-based virtual screening, stability filtering, structural modeling, molecular dynamics (MD) simulations, and ML-based binding affinity prediction** to accelerate peptide design for **therapeutics, diagnostics, and biosensors**.  

---

## Workflow Modules  

1. **Peptide Library Generation**  
   Create large-scale peptide libraries (thousands to millions of variants) via class-wise or all-residue mutagenesis.  
   🔗 [Open in Google Colab](https://colab.research.google.com/drive/1hN0-RLH3ro1VP1vC392WVyvTitaqKsdC?usp=sharing)  

2. **Peptide Preprocessing & Stability Filtering**  
   Prepare sequences, remove duplicates, and assess stability using GRAVY-based indices.  
   🔗 [Open in Google Colab](https://colab.research.google.com/drive/18g6FGDIXmfAimDCv0Nrm90l3l88WuOc-?usp=sharing)  

3. **Binding Affinity Prediction (PBEE)**  
   Estimate peptide–protein binding free energies (ΔG) after MD refinement using a machine learning scoring function.  
   🔗 [Open in Google Colab](https://colab.research.google.com/drive/1lu1dC0yRltKK_Wp-gF26oHcZSCiHaI8b?usp=sharing)  

4. **Peptide Analyzer Tool (Thermo Fisher Scientific)**  
   Evaluate peptide physicochemical stability, solubility, and synthesis feasibility.  
   🔗 [Peptide Analyzer Tool](https://www.thermofisher.com/in/en/home/life-science/protein-biology/peptides-proteins/custom-peptide-synthesis-services/peptide-analyzing-tool.html)  

---

## Case Studies  

AIoptide was validated across **four experimentally resolved protein–peptide complexes**:  

- **Case Study 1 (1T63)** – Androgen Receptor with GRIP1 NR box3 peptide  
- **Case Study 2 (1T5Z)** – Androgen Receptor with ARA70 coactivator  
- **Case Study 3 (1X7J)** – Estrogen Receptor β with coactivator peptide  
- **Case Study 4 (3O34)** – p53 tumor suppressor with coactivator peptide  

Each case study folder in this repository contains:  
- Generated peptide libraries  
- PepCNN screening results  
- GRAVY stability analysis  
- Structural models (CHIMERA_AA)  
- MD trajectories (AMBER24)  
- PBEE binding affinity predictions  

---

## ⚙️ How to Run  

Clone the repository:  

```bash
git clone https://github.com/Computational-biolab/AIoptide.git
cd AIoptide

PBEE reference:
Chaves, E. J. F., et al. Estimating absolute protein–protein binding free energies by a super learner model.
J. Chem. Inf. Model. (2025).
